# Performance Tuning

([Source](https://www.c-sharpcorner.com/UploadFile/ff2f08/tips-to-improve-sql-database-performance/))

#### 1. Do not use \* with select statement

SQL Server converts \* into all column names of the table before query execution. Instead of doing this, pass the name of the columns that are really required in query results.

```sql
--Bad practice

SELECT * FROM Table1
```

```sql
--Good practice

SELECT Column1, Column2, Column3 FROM Table1
```

#### 2. Use EXISTS instead of IN

EXISTS returns true if a sub query contains any rows else returns false. EXISTS is faster than the IN Query because for the IN Query SQL first collects all the data of the sub query. With EXISTS, the sub query does not produce actual query results. EXISTS is faster than IN only when sub query result is very large. IN is faster than EXISTS, when sub query result is very small

```sql
--Bad practice
SELECT  Column1, Column2, Column3 FROM Table1 WHERE Column1 IN (SELECT Column1 FROM Table2)
```

```sql
--Good practice
SELECT  Column1, Column2, Column3 FROM Table1 WHERE EXISTS (SELECT Column1 FROM Table2 Where Table2.Column1 = Table1.Column1)
```

#### 3. Select Appropriate Data Type of table columns

The selection of appropriate data types may help us to improve the SQL query performance. For example, I have an Employee Table and it has a code field. The length of the code may vary from 3 to 8. In this case, instead of selecting CHAR (8) we can use the VARCHAR (8) data type. Try to choose the smallest data type that works for each column. Try choosing an appropriate data type of a column to avoid explicit and implicit conversions, because both are costly in terms of time to take for conversion.

#### 4. Use proper join type

Select proper join type and join order. An Outer join is a more expensive process than the inner join. An Outer join must do everything that an Inner join does plus extra work for null extending results.

#### 5. Use Indexed Views

When we have a SQL Query that contains multiple joins between tables that do not change frequently (example lookup table), we can define an indexed view for better performance. An Index view is a view stored physically like a table. The Index view is updated by SQL Server itself when a table is modified that is used as part of the index view.&#x20;

#### 6. Do not use Count (\*)

Do not use Count (\*) when you require a row count. Instead of this, you can use Count (1) or Count (ColumnName).

```sql
--Bad practice
SELECT  COUNT(*) FROM Table1
```

```sql
--Good practice
SELECT  COUNT(1) FROM Table1
SELECT  COUNT(Column1) FROM Table1
```

#### 7. Avoid use of cursors

A Cursor is used to perform a function row by row. The Cursor forces the database engine to repeatedly fetch the rows, managing the locks and transmit the results. Forward-only and read-only cursors are faster and uses the least resources. If there is a primary key on a table then we can use a while loop. Try to avoid the use of a cursor on temp tables.

#### 8. Use a Table variable or CTE (Common Table Expression) instead of Temp Table whenever possible

Temp tables are stored physically in TempDB and they are permanent tables that are deleted after the session ends. CTE and Temp variables are created within memory. Note that CTE is not a replacement of a Table variable and a Temp table.

#### 9. Use SET NOCOUNT ON in Stored Procedure

The SET NOCOUNT ON statement prevents SQL Server from sending a message after each statement in a Stored Procedure. These messages are sent using a DONE\_IN\_PROC token. Each message contains the number of the row affected the row by the last executed SQL statement.

```sql
--Example
CREATE PROCEDURE [dbo].[MyTestProcedure]
(
   @para1 INT
)
AS
BEGIN
   SET NOCOUNT ON
   -- Body of stored procedure.
END
```

#### 10. Do not use "SP\_" prefix with any user define Stored Procedure name

In SQL Server, the master database has a Stored Procedure with the "sp\_" prefix, so SQL Server always looks first in the master database. If we use the "sp\_" prefix for any user define Stored Procedure and put it in a database other than master, the master database is still checked first.

#### 11. Use Stored Procedure for Complex Query and frequently used query

A Stored Procedure in SQL Server is a group of T-SQL statements. By default a Stored Procedure is precompiled, in other words a stored procedure is compiled when it executes the first time and also creates an execution plan that for subsequent calls of the Stored Procedure because the query processor does not need to create a new plan hence it takes less time to execute.

#### 12. Use Parameterized Query

The SQL Server saves execution plan for parameterized queries. This allows it to be reused on later execution.

#### 13. Use Try...Catch Block whenever required

A TRY...CATCH block is used for error handling in T-SQL statements. Use TRY...CATCH blocks whenever you work with transactions because if an error occurs during a transaction then it may cause a deadlock.

```sql
--Example
BEGIN TRAN Test
BEGIN TRY
      -- Do something
      COMMIT TRAN Test
END TRY
BEGIN CATCH
      ROLLBACK TRAN Test
END CATCH
```

#### 14. Select appropriate life of transaction (Try to Avoid long running transaction)

Keep your transactions as short as possible because locks are held during the transaction. Do not forget to commit or roll back the transaction before session end.

#### 15. Use proper Isolation level

The Transaction isolation level defines the degree to which one transition must be isolated from a resource and data modification made by another transaction. Isolation level is responsible for deciding how long read locks are held on a data row. A lower isolation level increases the ability to access the same data at the same time for many users but it increases the chance of a dirty read or loss of updated data. A higher isolation level decreases this type of concurrency issues but requires more database resources. So it is necessary to choose the appropriate isolation level for our transactions.

#### 16. Do not use function in WHERE Clauses

When a function is used with a select statement, it is not a bad thing because it returns powerful data with each row. But a function used with a WHERE clause forces SQL Server to do a table scan to determine the correct data.

#### 17. Try to avoid Expensive operators such as "LIKE", "NOT LIKE", Not equal to (<> or! =)

The Like Operator used to determine whether a specific character or string matches a specified pattern. This pattern may include regular characters or wildcard characters. The "Like" Operator always causes a table scan. This type of table scan is very expensive. Operators such as <> or NOT LIKE are also very costly in terms of performance.

#### 18. Define Relationships and Constraints whenever required

Primary key and foreign key relationships help us to ensure that we write optimal queries. SQL Server creates an optimal execution plan if the primary key and foreign key constraints are defined in the database schema.

#### 19. Create Index on All Foreign Keys

Mostly Foreign keys are used in joins, so if an index creates on foreign keys always beneficial.

#### 20. Create Index whenever required

Creating Indexes are one of the best ways to improve the performance of a SQL query. A table scan is done when no index is available on a table to help a SQL query. Some points must be kept in mind when creating an index.

* Do not create an index on columns that contain a high number of null values.
* Do not create indexes on columns that are frequently manipulated.
* Keep an index key short.
* Create indexes with a minimum percentage of duplicated values.

#### 21. Avoid Table and Index Scans

A Table and Index scan is an expensive process and it becomes more expensive the data size is greater. Select tables for scans that have few rows and a cluster index scan may be an effective option for some queries.

#### 22. Use multiple small indexes rather than a few wide indexes

We can create multiple indexes per table in SQL Server. Small or Narrow indexes provide more options than a wide composite index. Note that in an index, statistics are only kept for the first column of a composite index, so multiple single-column indexes ensure statistics are also kept on that column.

#### 23. Create indexes on columns used in "WHERE", "ORDER BY", "GROUP BY" and "DISTINCT" clauses

Create an index on columns used in a WHERE clause and used in aggregate operations, such as GROUP BY, DISTINCT, ORDER BY, MIN, MAX and so on.

#### 24. Remove unused indexes

Remove all unused indexes. An index is needed to be maintained even if they are not used.

### 25. Use ITW (Index Tuning Wizard)

The Index Tuning Wizard is used to obtain guidance and tips on index options. This is good way to create efficient indexes.

#### 26. Avoid long actions in triggers

A Trigger is always a part of a DML statement (INSERT, UPDATE or DELETE) and calling the transaction. A long-running action may cause a lock to be held longer than intended hence the result is the blocking of other queries. We can use a message queue to do long-running actions (accomplish this task asynchronously).

#### 27. Estimate the Hash Joins

Hash joins are used for many types of set matching operations such as inner join, outer join (left, right and full), intersection and union. In the absence of an index, a Hash Join is the best option. Evaluate the execution plan if you have many of hash joins to determine CPU usage.
