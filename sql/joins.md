# Joins

{% hint style="info" %}
Since solving any reasonable SQL problem requires a combination of all the topics covered here, hence it becomes difficult to seggregate problems based on one topic alone. So for SQL we are creating a dedicated **Problems** section. Theoritical and Basic questions will still be under their dedicated sections.
{% endhint %}

Joins are best explained using Venn diagrams

<figure><img src="../contents/SQL/images/image1.png" alt=""><figcaption><p>TSQL JOIN Types, <a href="https://stevestedman.com/2015/05/tsql-join-types-poster-version-4-1/">Reference</a></p></figcaption></figure>

Remember that in case of multiple joins each single join produces a **single derived table** that is then joined to the next table and so on.

## Questions

<details>

<summary>Address of People</summary>

**Reference -** [**Leetcode**](https://leetcode.com/problems/combine-two-tables/)

<pre><code><strong>Table: Person
</strong>
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

AddressId is the primary key column for this table.</code></pre>

Write a SQL query for a report that provides the following information for each person in the Person table, regardless of if there is an address for each of those people:

FirstName, LastName, City, State

**Answer**

```sql
select a.FirstName, a.LastName, b.City, b.State
from Person a
left join Address b
on a.PersonId = b.PersonID
```

</details>
