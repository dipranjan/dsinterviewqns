---
html_meta:
  "description lang=en": "Interview resource of Data Science focusing on Time and related functions."
  "keywords": "interview, data science, machine learning, Time"
  "property=og:locale": "en_US"
---


## Time

```{note}
Since solving any reasonable SQL problem requires a combination of all the topics covered here, hence it becomes difficult to seggregate problems based on one topic alone. So for SQL we are creating a dedicated **Problems** section. Theoritical and Basic questions will still be under their dedicated sections.
```

```{warning}
The below commands are for SQL Server, a lot of databases tend to do the Time part of things a little differently, many of them has additional commands or does not support a few commands. Please be cautious as the commands might change depending on the DB you are using.
```
**Reference:** [📖Explanation](https://www.sqlshack.com/learn-sql-sql-server-date-and-time-functions/)

In most product companies like Google, Salesforce, Facebook, etc. in short any company that deals with user interaction will store data about user interaction and more often than not will ask questions which leverages the querying or manipulating time part of stored data. While time part is not very difficult to solve people face problems in that they donot remember the right command to do what they are trying, so here we will share the list of common commands along with their intended usage.

To get system values:

- `GETDATE()` or `CURRENT_TIMESTAMP` : return the datetime value from the server where SQL Server runs
- `SYSDATETIME()` : same as above but with more precision

Next we will see how can we extract specific feature from a date column:

- `YEAR('2021/07/06 14:08:52')` or `DATEPART(YEAR, '2021/07/06 14:08:52')` or `DATENAME(YEAR, '2021/07/06 14:08:52')` : will return the year
- Same command can be used for MONTH, DAY, HOUR, MINUTE, SECOND
- DATENAME for Month will return the name of the month

The next 3 functions are used to create date or modify/combine dates:

- `DATEFROMPARTS(year, month, day)` takes a year, month and day as integer values and creates 1 date out of them.
- `DATEADD(date_part, interval, date)` takes 3 arguments and returns a date that is interval (date_parts) number of given units (date_part) distant from the given date (date)
- `DATEDIFF(date_part, start_date, end_date)` returns the number of units (date_part) between end_date and start_date (end_date – start_date).