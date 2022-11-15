# Temporary Datasets

{% hint style="info" %}
Since solving any reasonable SQL problem requires a combination of all the topics covered here, hence it becomes difficult to seggregate problems based on one topic alone. So for SQL we are creating a dedicated **Problems** section. Theoretical and Basic questions will still be under their dedicated sections.
{% endhint %}

**Reference:** [📖Explanation](https://www.red-gate.com/simple-talk/databases/sql-server/t-sql-programming-sql-server/sql-server-cte-basics/)

Sometimes in order to ease things out you need to create a temporary version of the data for either viewing it or for running some further calculations to it. Now if it is just that you want to run the same query daily and get the results you might as well save it as a `VIEW` . **You can consider view as a SQL statement saved with a name**.

While it is very important to know what a `VIEW` is, however in most cases the ask will be to solve some question which for which you need to create a temporary dataset and run queries on that. You can use Common Table Expression or CTE for that. It uses the `WITH` keyword.

**CTE can be of 2 types:**

* A **recursive CTE** is one that references itself within that CTE. The recursive CTE is useful when working with hierarchical data because the CTE continues to execute until the query returns the entire hierarchy
* A **non-recursive CTE** is one that does not reference itself within the CTE. Nonrecursive CTEs tend to be simpler than recursive CTEs

<figure><img src="../.gitbook/assets/image4 (1).png" alt=""><figcaption><p>The above image shows a case where we need to use CTE to answer a question</p></figcaption></figure>
