# Functions & Stored Proc

{% hint style="info" %}
Since solving any reasonable SQL problem requires a combination of all the topics covered here, hence it becomes difficult to segregate problems based on one topic alone. So, for SQL we are creating a dedicated [**Problems**](problems.md) section. Theoretical and Basic questions will still be under their dedicated sections.
{% endhint %}

Functions are calculated values that cannot make lasting modifications to SQL Server's environment (i.e., no INSERT or UPDATE statements allowed).

If a function provides a scalar value, it may be used inline in SQL queries; if it returns a result set, it can be joined on.

Functions must return a value and cannot change the data they receive as parameters, as defined by computer science (the arguments). Functions can't modify anything and must have at least one parameter. They also have to return a result. Stored procedures don't need a parameter, may modify database objects, and don't have to return a result.

Stored procedures are used to connect SQL queries in a transaction and to communicate with the outside world.

```sql
CREATE PROCEDURE SelectAllCustomers @City nvarchar(30), @PostalCode nvarchar(10)
AS
SELECT * FROM Customers WHERE City = @City AND PostalCode = @PostalCode

-- To run the Stored Proc
EXEC SelectAllCustomers @City = 'London', @PostalCode = 'WA1 1DP';
```

<details>

<summary>N-th Highest Salary</summary>

**Reference -** [**Leetcode**](https://leetcode.com/problems/nth-highest-salary/) Write a SQL query to get the Nth highest salary from the Employee table.

```
| Id | Salary |
|----|--------|
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
```

For example, given the above Employee table, the query should return 200 as the second highest salary (N =2). If there is no second highest salary, then the query should return null.

**Answer**

Multiple solutions are possible only one approach is given below for reference

```sql
	CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
	BEGIN
	      DECLARE temp INT;
	      SET temp = N-1;
	  RETURN (      
	      Select DISTINCT Salary from Employee
	      Order by Salary Desc
	      LIMIT 1 Offset temp      
	  );
	END
```

</details>
