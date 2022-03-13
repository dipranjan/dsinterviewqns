---
html_meta:
  "description lang=en": "Interview resource of Data Science Interview focusing on Excel basics."
  "keywords": "interview, Excel, practice questions"
  "property=og:locale": "en_US"
---

## Data Manipulation

```{warning}
This page is a work in progress
```

```{note}
Excel, as a product, always remains under active development from Microsoft. With new releases, new features are brought in whereas old ones are discarded. Due to this there might be changes to the solutions mentioned below depending on the version that you are using.
```

```{admonition} Problem: SUM of Digits in a cell
:class: tip, dropdown

Can you write a formula to generate the SUM of all digits in a cell?
```

```{admonition} Solution:
:class: dropdown

![Solution](../Excel/images/image5.PNG)

To use when you are sure that there are only digits in the column: 

`
	=SUMPRODUCT(--MID(B2,ROW(INDIRECT("1:"&LEN(B2))),1))
`

But if there are other characters too use this: 

`
	=SUMPRODUCT((LEN(B3)-LEN(SUBSTITUTE(B3,ROW(1:9),"")))*ROW(1:9))
`
 
```

```{admonition} Problem: Uniqueness Check
:class: tip, dropdown

Given the data below, please answer the following questions

| Region | ID |
|--------|----|
| A      | 1  |
| B      | 2  |
| C      | 3  |
| C      | 4  |
| B      | 3  |
| C      | 4  |

This is a 3 part question:

- Given a table of data how do you tell if it has duplicates?
- Create a table with distinct values from this
- Can you do a conditional duplicate check on this table?
```

```{admonition} Solution:
:class: dropdown

![Solution](../Excel/images/image6.PNG)

You can check for duplicates using:

`
= COUNTIF($B$2:$B$7)
`
Rows with value > 1 has duplicates

Inorder to create a table with Unique values there are 2 ways:

- Select the table and click on remove duplicates

![Solution](../Excel/images/image7.PNG)

- If you want to keep the source table and create the unique value table elsewhere use:

`
=UNIQUE(A2:B7)
`
 
Conditional check can be done using IF clause, for example if you want to check duplicates only for ID > 3 you can use something like:

`
=IF(B2>3,COUNTIF($B$2:$B$7,B4),0)
`
 
```