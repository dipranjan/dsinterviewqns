## Select


```{admonition} Problem:
:class: tip

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
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
`

```