---
html_meta:
  "description lang=en": "Interview resource of Data Science focusing on Windows Functions."
  "keywords": "interview, data science, machine learning, SQL, Windows functions"
  "property=og:locale": "en_US"
---


## Windows Functions

```{note}
Since solving any reasonable SQL problem requires a combination of all the topics covered here, hence it becomes difficult to seggregate problems based on one topic alone. So for SQL we are creating a dedicated **Problems** section. Theoritical and Basic questions will still be under their dedicated sections.
```

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
