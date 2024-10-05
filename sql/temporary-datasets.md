---
description: A summary of Temp Table vs Table variable vs CTE
---

# Temporary Datasets

{% hint style="info" %}
Since solving any reasonable SQL problem requires a combination of all the topics covered here, hence it becomes difficult to seggregate problems based on one topic alone. So for SQL we are creating a dedicated [**Problems**](problems.md) section. Theoretical and Basic questions will still be under their dedicated sections.
{% endhint %}

**Reference:** [📖Explanation](https://www.red-gate.com/simple-talk/databases/sql-server/t-sql-programming-sql-server/sql-server-cte-basics/)

Sometimes in order to ease things out you need to create a temporary version of the data for either viewing it or for running some further calculations to it. Now if it is just that you want to run the same query daily and get the results you might as well save it as a `VIEW` . **You can consider view as a SQL statement saved with a name**.

While it is very important to know what a `VIEW` is, however in most cases the ask will be to solve some question which for which you need to create a temporary dataset and run queries on that. You can use Common Table Expression or CTE for that. It uses the `WITH` keyword.

### **CTE**&#x20;

CTE can be of 2 types:

* A **recursive CTE** is one that references itself within that CTE. The recursive CTE is useful when working with hierarchical data because the CTE continues to execute until the query returns the entire hierarchy
* A **non-recursive CTE** is one that does not reference itself within the CTE. Nonrecursive CTEs tend to be simpler than recursive CTEs

<figure><img src="../_build/html/_images/image44.PNG" alt=""><figcaption><p>The above image shows a case where we need to use CTE to answer a question</p></figcaption></figure>

### Table Variable

This biggest difference is that a CTE can only be used in the current query scope whereas a temporary table or table variable can exist for the entire duration of the session allowing you to perform many different DML operations against them.

### Compare Temp Table, Table Variable and CTE

([Source](https://www.c-sharpcorner.com/UploadFile/ff2f08/tips-to-improve-sql-database-performance/))

```sql
-- CTE
WITH t (customerid, lastorderdate) AS 
 (SELECT customerid, max(orderdate) 
  FROM sales.SalesOrderHeader
  GROUP BY customerid)
SELECT * 
FROM sales.salesorderheader soh
INNER JOIN t ON soh.customerid=t.customerid AND soh.orderdate=t.lastorderdate
GO

-- Temporary table
CREATE TABLE #temptable (customerid [int] NOT NULL PRIMARY KEY, lastorderdate [datetime] NULL);

INSERT INTO #temptable
SELECT customerid, max(orderdate) as lastorderdate 
FROM sales.SalesOrderHeader
GROUP BY customerid;

SELECT * 
FROM sales.salesorderheader soh
INNER JOIN #temptable t ON soh.customerid=t.customerid AND soh.orderdate=t.lastorderdate

DROP TABLE #temptable
GO

-- Table variable
DECLARE @tablevariable TABLE (customerid [int] NOT NULL PRIMARY KEY, lastorderdate [datetime] NULL);

INSERT INTO @tablevariable
SELECT customerid, max(orderdate) as lastorderdate 
FROM sales.SalesOrderHeader
GROUP BY customerid;

SELECT * 
FROM sales.salesorderheader soh
INNER JOIN @tablevariable t ON soh.customerid=t.customerid AND soh.orderdate=t.lastorderdate
GO
```

Looking at [SQL Profiler](https://www.mssqltips.com/sql-server-tip-category/83/profiler-and-trace/) results from these queries (each were run 10 times and averages are below) we can see that the CTE just slightly outperforms both the temporary table and table variable queries when it comes to overall duration. The CTE also uses less CPU than the other two options and performs fewer reads (significant fewer reads that the table variable query).

| Query Type     | Reads  | Writes | CPU | Duration (ms) |
| -------------- | ------ | ------ | --- | ------------- |
| CTE            | 1378   | 0      | 47  | 497           |
| Temp table     | 2146   | 51     | 109 | 544           |
| Table variable | 133748 | 51     | 297 | 578           |

\
