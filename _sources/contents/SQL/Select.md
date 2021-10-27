## SQL Basics

If you are new to SQL [this ▶️](https://www.youtube.com/watch?v=7GVFYt6_ZFM&list=PL08903FB7ACA1C2FB) is one of the most comprehensive material of SQL that is available in the internet. Please go through the portions of interest to you.

### DDL

DDL stands for Data Defination Language. These commands are used to change the structure of a database and database objects.
Some common commands are as follows:
- **CREATE:** is used to create the database or its objects (like table, index, function, views, store procedure and triggers).

	The generic format of the create table is as follows:

	```sql
	CREATE DATABASE databasename;

	CREATE TABLE table_name (
	column1 datatype CONSTRAINT,
	column2 datatype CONSTRAINT,
	column3 datatype CONSTRAINT); 
	```

	Using constraints we can specify the limit on the type of data that can be stored in a particular column in a table. Some of the constraints are:

	- **NOT NULL:** This constraint tells that the value of a column cannot be null.
	- **UNIQUE:** This constraint tells that the values in any row of a column must not be repeated.
	- **PRIMARY KEY:** A primary key is a field which can uniquely identify each row in a table. We can say that PRIMARY KEY is combination of NOT NULL and UNIQUE constraints. A table can have only one field as primary key.
	- **FOREIGN KEY:** Foreign Key is a field in a table which uniquely identifies each row of another table. This field points to primary key of another table. This usually creates a relation between the tables.
	- **CHECK:** This constraint helps to ensure that the value stored in a column meets a specific condition.
	- **DEFAULT:** This constraint specifies a default value for the column when no value is specified by the user.

- **DROP:** is used to delete databases or tables.
- **ALTER:** is used to alter the structure of the database. You can use this to add/modify/delete a column.
- **TRUNCATE:** The TRUNCATE TABLE statement is used to delete the data inside a table, *but not the table itself.*
- **RENAME:** is used to rename an object existing in the database.

### Referential Integrity

Referential integrity is a property of data stating references within it are valid. In the context of relational databases, it requires every value of one attribute (column) of a relation (table) to exist as a value of another attribute (column) in a different (or the same) relation (table).
For referential integrity to hold in a relational database, any column in a base table that is declared a foreign key can contain either a null value, or only values from a parent table's primary key or a candidate key. In other words, when a foreign key value is used it must reference a valid, existing primary key in the parent table. For instance, deleting a record that contains a value referred to by a foreign key in another table would break referential integrity. Some relational database management systems (RDBMS) can enforce referential integrity, normally either by deleting the foreign key rows as well to maintain integrity, or by returning an error and not performing the delete. Which method is used may be determined by a referential integrity constraint defined in a data dictionary.

### UNION & UNION ALL

- UNION removes duplicate rows, UNION ALL doesnot
- UNION has to perform a distinct sort to remove duplicates, hence is a little slow
- UNION combines rows of two tables, JOIN combines columns

### NULL

There are 3 ways to take care of NULL values:

Let's take an example suppose we want to fill the Manager name as 'No Manager' if an employee does have a manager assigned in the manager column. This can be done using:
- ``` ISNULL(manager, 'No Manager') ```
- ``` CASE WHEN manager IS NULL THEN 'No Manager' ELSE manager END as manager ```
- The other option is ``` COALESCE ``` but it esentially takes the first non-null value out of the passed columns



### Questions

```{admonition} Problem: [Leetcode] Second Highest Salary
:class: tip, dropdown

**Reference - [Leetcode](https://leetcode.com/problems/second-highest-salary/)**

*For a similar problem with different approach check Nth highest salary problem*

Write a SQL query to get the second highest salary from the Employee table.

| Id | Salary |
|----|--------|
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |

For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

```

````{admonition} Solution:
:class: dropdown

Multiple solutions are possible only one approach is given below for reference

```sql
SELECT
(SELECT DISTINCT(Salary)
FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1) 
AS SecondHighestSalary
```

````

```{admonition} Problem: [MICROSOFT] HAVING vs WHERE
:class: tip, dropdown

**Asked By - MICROSOFT**

Can you elborate on the differences between HAVING and WHERE clause in a SQL query?

```

```{admonition} Solution:
:class: dropdown

The major differences between between HAVING and WHERE are as follows:

- WHERE can be used with Select, Insert, Update, Delete statements. HAVING can only be used with Select statements
- WHERE filters rows before aggregation, HAVING filters after that

Performance wise there is not much of a difference, the best practice is to filter out unwanted rows as early as possible
```
