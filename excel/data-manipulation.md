# Data Manipulation

{% hint style="warning" %}
This page is a Work in Progress
{% endhint %}

{% hint style="info" %}
Excel, as a product, always remains under active development from Microsoft. With new releases, new features are brought in whereas old ones are discarded. Due to this there might be changes to the solutions mentioned below depending on the version that you are using.
{% endhint %}

<details>

<summary>SUM of digits</summary>

Can you write a formula to generate the SUM of all digits in a cell?

**Answer**

![](../contents/Excel/images/image5.png)

To use when you are sure that there are only digits in the column:

`=SUMPRODUCT(--MID(B2,ROW(INDIRECT("1:"&LEN(B2))),1))`

But if there are other characters too use this:

`=SUMPRODUCT((LEN(B3)-LEN(SUBSTITUTE(B3,ROW(1:9),"")))*ROW(1:9))`

</details>

<details>

<summary>DISTINCT &#x26; Duplicates</summary>

Given the data below, please answer the following questions

This is a 3-part question:

* Given a table of data how do you tell if it has duplicates?
* Create a table with distinct values from this
* Can you do a conditional duplicate check on this table?

```markup
| Region | ID |
|--------|----|
| A      | 1  |
| B      | 2  |
| C      | 3  |
| C      | 4  |
| B      | 3  |
| C      | 4  |
```

**Answer**

![](../\_build/html/\_images/image62.PNG)****

You can check for duplicates using:

`= COUNTIF($B$2:$B$7)` Rows with value > 1 has duplicates

In order to create a table with Unique values there are 2 ways:

* Select the table and click on remove duplicates
* If you want to keep the source table and create the unique value table, elsewhere use:

`=UNIQUE(A2:B7)`

Conditional check can be done using IF clause, for example if you want to check duplicates only for ID > 3 you can use something like:

`=IF(B2>3,COUNTIF($B$2:$B$7,B4),0)`

</details>
