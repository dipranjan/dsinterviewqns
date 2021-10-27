## Windows Functions

**Reference:** [📖Explanation](https://www.red-gate.com/simple-talk/sql/t-sql-programming/introduction-to-t-sql-window-functions/), [🔫Playground](https://dbfiddle.uk/?rdbms=sqlserver_2017&fiddle=6379904805d1f465cc0f6ea33fc3c0d6)

Window (also, windowing or windowed) functions perform a calculation over a set of rows. I like to think of “looking through the window” at the rows that are being returned and having one last chance to perform a calculation. The window is defined by the OVER clause which determines if the rows are partitioned into smaller sets and if they are ordered.
They allow you to add your favourite aggregate function to a non-aggregate query. Similar to Transform is pandas group by clause.

### Common Windows Functions

- **Ranking functions**
	- **ROW_NUMBER:** is used to add unique row numbers to a partition or to the entire result set. It has the ability to turn non-unique rows into unique rows
	- **RANK:** it will give numbers same as row_number just that same data will get same rank
	- **DENSE_RANK:** doesnot skip and rank number
	- **NTILE:** It assigns bucket numbers to the rows instead of row numbers or ranks

```{figure} ../SQL/images/image2.PNG
---
name: image2
---
Ranking functions, check playground to work with this
```

- **Offset functions**
	- **LAG:**  the function allows you to pull columns or expressions from a row before the current row
	- **LEAD:** the function allows you to pull columns or expressions from a row after the current row
	- **FIRST_VALUE:** the functions allows you to return values from the first row of the partition
	- **LAST_VALUE:** the functions allows you to return values from the last row of the partition

- **Statistical functions**
 	– **PERCENT_RANK:** returns the percentage of rows that rank lower than the current row, its formula is $\frac{\text{Rank} -1}{\text{Row count} -1}$
 	- **CUME_DIST:** cumulative distribution, returns the exact rank, its formula is $\frac{\text{Rank}}{\text{Row count}}$
 	- **PERCENTILE_DISC & PERCENTILE_CONT:** these two work in the opposite way. Given a percent rank, find the value at that rank. They differ in that PERCENTILE_DISC will return a value that exists in the set while PERCENTILE_CONT will calculate an exact value if none of the values in the set falls precisely at that rank. You can use PERCENTILE_CONT to calculate a median by supplying 0.5 as the percent rank. For example, which temperature ranks at 50% in St. Louis?


**One problem is you cannot add window functions to the WHERE clause.**

### Questions

```{admonition} Problem: [Leetcode] Rank Scores
:class: tip, dropdown

**Reference - [Leetcode](https://leetcode.com/problems/rank-scores/)**

Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.

| Id | Score |
|----|-------|
| 1  | 3.40  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.50  |
| 5  | 4.00  |
| 6  | 3.65  |

For example, given the above Scores table, your query should generate the following report (order by highest score):

| score | Rank    |
|-------|---------|
| 4.00  | 1       |
| 4.00  | 1       |
| 3.95  | 2       |
| 3.65  | 3       |
| 3.65  | 3       |
| 3.40  | 4       |

```

````{admonition} Solution:
:class: dropdown

The tie resolving method which is being asked in the question is called Dense Rank, if we use Rank it will have "holes"

```sql
select 
Score, dense_rank() over(order by score desc) as Rank
from Scores
```

````


```{admonition} Problem: [CHEWY] 2nd Highest score
:class: tip, dropdown

| Id | subject | marks |
|---:|---------|------:|
|  1 | Maths   |    30 |
|  1 | Phy     |    50 |
|  1 | Chem    |    85 |
|  2 | Maths   |    90 |
|  2 | Phy     |    50 |
|  2 | Chem    |    85 |

Select the second highest mark for each student.

```

````{admonition} Solution:
:class: dropdown

```sql
with CTE as(
	select *, rank() over(partition by Id order by marks desc) as Rank from tablename
)
select Id, subject, marks from CTE where Rank = 1
```
````



```{admonition} Problem: [Leetcode] Consecutive Numbers
:class: tip, dropdown

**Reference - [Leetcode](https://leetcode.com/problems/consecutive-numbers/)**


Write an SQL query to find all numbers that appear at least three times consecutively.

Return the result table in any order.

Input: 

Logs table:

| Id | Num |
|----|-----|
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |


Result table:

| ConsecutiveNums |
|-----------------|
| 1               |

1 is the only number that appears consecutively for at least three times.

```

````{admonition} Solution:
:class: dropdown

Multiple solutions are possible, one of them is given below
```sql
with a(Num,NextNum,SecondNextNum ) as(

	SELECT   Num
	         , LEAD(Num, 1) OVER (ORDER BY Id) AS NextNum
	         , LEAD(Num, 2) OVER (ORDER BY Id) AS SecondNextNum
	      FROM Logs
	      
	)

	select distinct(Num) as ConsecutiveNums from a
	where
	Num = NextNum
	and Num = SecondNextNum
```
````

```{admonition} Problem: [SALESFORCE] User Growth
:class: tip, dropdown

**[🔫Playground](https://dbfiddle.uk/?rdbms=sqlserver_2017&fiddle=ce4ded37fa37bf552365c18cb7840c3b)**

Given you have user data for 2 accounts for 2 months. Calculate the growth rate of users in each account where growth rate is defined as unique users in month 2 divided by unique users in month 1.


```

````{admonition} Solution:
:class: dropdown

```sql
with cte as (
	select account_id, count(distinct(user_id)) as unique_user, MONTH(date_details) as user_month from tablename
	group by account_id, MONTH(date_details)
	)

select a.account_id,month_2,month_1,
cast((month_2/month_1)as float) as growth  from 
(select account_id, unique_user as month_1
from cte where user_month = 1)a
left join
(select account_id, unique_user as month_2
from cte where user_month = 2)b
on (a.account_id = b.account_id)
```

````

```{admonition} Problem: [SALESFORCE] Month over Month Revenue
:class: tip, dropdown

**[🔫Playground](https://dbfiddle.uk/?rdbms=sqlserver_2017&fiddle=72569e574e670b477d2f62fdfc4276ca)**

You have 2 tables:

 - transactions: date, prod_id, quantity
 - products: prod_id, price

 Calculate the month over month revenue, example month over month revenue for month2 is month2_Revenue- month1_Revenue


```

````{admonition} Solution:
:class: dropdown

```sql
with cte as(
	select MONTH(a.date_details) as month, sum(b.price*a.qty) as Rev
	from transactions a
	inner join products b
	on a.prod_id = b.prod_id
	group by MONTH(a.date_details)
	),

	cte2 as(
	select month, Rev, lag(Rev,1) over(order by month) as prev_month
	from cte
	)

select month, (Rev-Prev_month) as extra_rev  from cte2
where 
prev_month is not null
```

````


```{admonition} Problem: [SALESFORCE] Employee earning more than their manager
:class: tip, dropdown

**Reference - [Leetcode](https://leetcode.com/problems/employees-earning-more-than-their-managers/)**

Write an SQL query to find the employees who earn more than their managers.

| Id | Name  | Salary | ManagerId |
|---:|-------|-------:|----------:|
|  1 | Joe   |  70000 |         3 |
|  2 | Henry |  80000 |         4 |
|  3 | Sam   |  60000 |           |
|  4 | Max   |  90000 |           |

Output will be : Joe

```

````{admonition} Solution:
:class: dropdown
```sql
with cte as(
	Select a.Name as Employee, b.Name as Manager, a.Salary as Emp_Sal, b.Salary as Man_Salary
	from Employee a
	inner join Employee b
	on a.ManagerId = b.id)

Select Employee from cte where Emp_Sal > Man_Salary
```

````

```{admonition} Problem: [Leetcode] Highest Salary in each Department
:class: tip, dropdown

**Reference - [Leetcode](https://leetcode.com/problems/department-highest-salary/)**

Write an SQL query to find employees who have the highest salary in each of the departments.

![image 3](../SQL/images/image3.PNG)

```

````{admonition} Solution:
:class: dropdown

```sql
with cte as(
	select Name, Salary, DepartmentId,
	RANK() over(Partition by DepartmentId order by salary desc) as Rank
	from Employee
)
		    
select b.Name as Department, a.Name as Employee, a.Salary
from cte a
inner join Department b
on a.DepartmentId = b.Id
where a.Rank = 1
```

````

```{admonition} Problem: [AMAZON] Cumulative Sum
:class: tip, dropdown

Given a users table, write a query to get the cumulative number of new users added by day, with the total reset every month.

[🔫Playground](https://dbfiddle.uk/?rdbms=sqlserver_2017&fiddle=516b59f188aaf8c5c1296143d1b13bcd)

```

````{admonition} Solution:
:class: dropdown

```sql
Select Created_date
,SUM(Count(Id)) OVER(partition by month(Created_date) order by Created_date) as Total_users
from users
group by Created_date
```

````