## Functions

```{admonition} Problem: [Leetcode] Nth Highest Salary
:class: tip, dropdown

**Reference - [Leetcode](https://leetcode.com/problems/nth-highest-salary/)**
Write a SQL query to get the Nth highest salary from the Employee table.

| Id | Salary |
|----|--------|
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |

For example, given the above Employee table, the query should return 200 as the second highest salary (N =2). If there is no second highest salary, then the query should return null.

```

````{admonition} Solution:
:class: dropdown

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

````