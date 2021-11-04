---
html_meta:
  "description lang=en": "Interview resource of Data Science focusing on SQL, specifically JOINS."
  "keywords": "interview, data science, machine learning, SQL"
  "property=og:locale": "en_US"
---

## Joins

```{note}
Since solving any reasonable SQL problem requires a combination of all the topics covered here, hence it becomes difficult to seggregate problems based on one topic alone. So for SQL we are creating a dedicated **Problems** section. Theoritical and Basic questions will still be under their dedicated sections.
```

Joins are best explained using Venn diagrams

```{figure} ../SQL/images/image1.PNG
---
name: image1
---
TSQL JOIN Types, [Reference](https://stevestedman.com/2015/05/tsql-join-types-poster-version-4-1/)
```

Remember that in case of multiple joins each single join produces a **single derived table** that is then joined to the next table and so on.


### Questions

```{admonition} Problem: [Leetcode] Join 2 tables
:class: tip, dropdown

**Reference - [Leetcode](https://leetcode.com/problems/combine-two-tables/)**

Table: Person

| Column Name | Type    |
|-------------|---------|
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |

PersonId is the primary key column for this table.

Table: Address


| Column Name | Type    |
|-------------|---------|
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |

AddressId is the primary key column for this table.
 

Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:

FirstName, LastName, City, State

```

````{admonition} Solution:
:class: dropdown

```sql
select a.FirstName, a.LastName, b.City, b.State
from Person a
left join Address b
on a.PersonId = b.PersonID
```
````