# Basics

{% hint style="info" %}
Since solving any reasonable SQL problem requires a combination of all the topics covered here, hence it becomes difficult to seggregate problems based on one topic alone. So for SQL we are creating a dedicated [**Problems**](problems.md) section. Theoritical and Basic questions will still be under their dedicated sections.
{% endhint %}

If you are new to SQL, the video playlist below[️](https://www.youtube.com/watch?v=7GVFYt6\_ZFM\&list=PL08903FB7ACA1C2FB) is one of the most comprehensive materials of SQL that is available on the internet. Please go through the portions of interest to you.

{% embed url="https://www.youtube.com/watch?list=PL08903FB7ACA1C2FB&v=7GVFYt6_ZFM" %}

## DDL

DDL stands for Data Definition Language. These commands are used to change the structure of a database and database objects. Some common commands are as follows:

*   **CREATE:** is used to create the database or its objects (like table, index, function, views, store procedure and triggers).

    The generic format of the create table is as follows:

    ```sql
    CREATE DATABASE databasename;

    CREATE TABLE table_name (
    column1 datatype CONSTRAINT,
    column2 datatype CONSTRAINT,
    column3 datatype CONSTRAINT); 
    ```

    Using constraints, we can specify the limit on the type of data that can be stored in a particular column in a table. Some of the constraints are:

    * **NOT NULL:** This constraint tells that the value of a column cannot be null.
    * **UNIQUE:** This constraint tells that the values in any row of a column must not be repeated.
    * **PRIMARY KEY:** A primary key is a field which can uniquely identify each row in a table. We can say that PRIMARY KEY is combination of NOT NULL and UNIQUE constraints. A table can have only one field as primary key.
    * **FOREIGN KEY:** Foreign Key is a field in a table which uniquely identifies each row of another table. This field points to primary key of another table. This usually creates a relation between the tables.
    * **CHECK:** This constraint helps to ensure that the value stored in a column meets a specific condition.
    * **DEFAULT:** This constraint specifies a default value for the column when no value is specified by the user.
* **DROP:** is used to delete databases or tables.
* **ALTER:** is used to alter the structure of the database. You can use this to add/modify/delete a column.
* **TRUNCATE:** The TRUNCATE TABLE statement is used to delete the data inside a table, _but not the table itself._
* **RENAME:** is used to rename an object existing in the database.

## Referential Integrity

Referential integrity is a property of data stating references within it are valid. In the context of relational databases, it requires every value of one attribute (column) of a relation (table) to exist as a value of another attribute (column) in a different (or the same) relation (table). For referential integrity to hold in a relational database, any column in a base table that is declared a foreign key can contain either a null value, or only values from a parent table's primary key or a candidate key. In other words, when a foreign key value is used it must reference a valid, existing primary key in the parent table. For instance, deleting a record that contains a value referred to by a foreign key in another table would break referential integrity. Some relational database management systems (RDBMS) can enforce referential integrity, normally either by deleting the foreign key rows as well to maintain integrity, or by returning an error and not performing the delete. Which method is used may be determined by a referential integrity constraint defined in a data dictionary.

## UNION & UNION ALL

* UNION removes duplicate rows, UNION ALL does not
* UNION has to perform a distinct sort to remove duplicates, hence is a little slow
* UNION combines rows of two tables, JOIN combines columns

## NULL

There are 3 ways to take care of NULL values:

Let's take an example suppose we want to fill the Manager name as 'No Manager' if an employee does have a manager assigned in the manager column. This can be done using:

* `ISNULL(manager, 'No Manager')`
* `CASE WHEN manager IS NULL THEN 'No Manager' ELSE manager END as manager`
* The other option is `COALESCE` but it essentially takes the first non-null value out of the passed columns

### Best practices

* Use aliases to shorten and simplify names. This can make your code more readable and usable.&#x20;
* Avoid using the SELECT \* statement. This can cause unexpected results and performance issues.&#x20;
* Use indexes to speed up queries. Indexes allow the database to quickly find entries that match specific criteria.&#x20;
* Use EXIST() instead of COUNT(). EXIST() only runs until it finds the first entry for a record in the table. This can save time and computing power.&#x20;
* Avoid using SELECT DISTINCT for large tables. This clause removes duplicate entries, but it is computationally expensive.&#x20;
* Use WHERE instead of HAVING.&#x20;
* Use ORDER BY to ensure the ordering of your results.
* Use STARTS\_WITH instead of LIKE.&#x20;
* Avoid using multiple nested queries.
* Avoid using unnecessary subqueries.  Instead, rewrite queries with outer joins.&#x20;

## Questions

<details>

<summary>[MICROSOFT] Having vs Where</summary>

Can you elborate on the differences between HAVING and WHERE clause in a SQL query?

**Answer**

The major differences between HAVING and WHERE are as follows:

* WHERE can be used with Select, Insert, Update, Delete statements. HAVING can only be used with Select statements
* WHERE filters rows before aggregation, HAVING filters after that

Performance wise there is not much of a difference, the best practice is to filter out unwanted rows as early as possible.

</details>

<details>

<summary>DROP vs TRUNCATE vs DELETE</summary>

The DELETE command deletes one or more existing records from the table in the database. The DROP Command drops the complete table from the database. The TRUNCATE Command deletes all the rows from the existing table, leaving the row with the column names.

</details>

Can you tell the difference between T-SQL and PL SQL

**Answer**

| \*\*T-SQL\*\*                                                                                                                                                        | \*\*P/L SQL\*\*                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| T-SQL   was originally developed by Sybase and now owned by Microsoft. Hence, it   works with Microsoft SQL Server only.                                             | P/L SQL was developed   by Oracle and works with Oracle only.                                                              |
| All   database objects like Tables/Views/Procedures are internally organized by   database names. Users are allowed access to a specific database and its   objects. | All database objects   are organized in Schemas. Users are allowed access to certain schemas via   roles and permissions.  |
| More   focussed on Microsoft SQL Server and its functions only.                                                                                                      | P/L SQL is more   versatile and encompassing, E.g. you can send Emails and access Web   Pages.                             |
| Allows   B-Tree Indexes only.                                                                                                                                        | Allows B-Tree, Bitmap,   Domain, and Partitioned Indexes.                                                                  |
| Provides   a greater degree of control on how an application works in Microsoft SQL   Server and is easy to learn.                                                   | Enhances the power of   plain SQL, and is considered to be more powerful and holistic.                                     |
| Limited   and patchy support for use of Cursors.                                                                                                                     | Powerful support for   use of Cursors, the underlying file/data organization supports it.                                  |
| No   direct support for Object-Oriented programming. Only supported though 3rd   party ORM   tools.                                                                  | Full support for Object-Oriented programming via Function Overloading, Data Encapsulation, etc.                            |
| Explicit   error handling capabilities using Try-Catch blocks.                                                                                                       | Provides error handling via checking for Exceptions only.                                                                  |
| Provides bulk insert and data loading.                                                                                                                               | No explicit bulk inserts.                                                                                                  |
| Allows reading data from an external sequential file and you can use the BULK   statement to fine-tune the external reads.                                           | Indirectly allows reading data from an external sequential file but no specific language   constructs to ease the process. |
| No packages to ease re-use.                                                                                                                                          | Allows grouping of Procedures into Packages, which can be reused.                                                          |
| No   need for Subqueries and DELETE and UPDATE are improvised accordingly.                                                                                           | Needs Subqueries to read data from another table.                                                                          |
| Provides WAITFOR construct to wait for a certain period of elapsed time.                                                                                             | No such direct construct in P/L SQL.                                                                                       |
| No support for Arrays.                                                                                                                                               | Supports Arrays.                                                                                                           |

