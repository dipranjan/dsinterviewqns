## Windows Functions


```{admonition} Problem: Rank Scores
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

```{admonition} Solution:
:class: dropdown

The tie resolving method which is being asked in the question is called Dense Rank, if we use Rank it will have "holes"

`
select 
Score, dense_rank() over(order by score desc) as Rank
from Scores
`

```

```{admonition} Problem: Consecutive Numbers
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

```{admonition} Solution:
:class: dropdown

Multiple solutions are possible, one of them is given below

`
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
`

```