## SQL Basics





### Questions

```{admonition} Problem: [Leetcode] Second Highest Salary
:class: tip, dropdown

**Reference - [Leetcode](https://leetcode.com/problems/second-highest-salary/)**
** For a similar problem with different approach check Nth highest salary problem **

Write a SQL query to get the second highest salary from the Employee table.

| Id | Salary |
|----|--------|
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |

For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

```

```{admonition} Solution:
:class: dropdown

Multiple solutions are possible only one approach is given below for reference

	`
	SELECT
	(SELECT DISTINCT(Salary)
	FROM Employee
	ORDER BY Salary DESC
	LIMIT 1 OFFSET 1) 
	AS SecondHighestSalary
	`

```

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
