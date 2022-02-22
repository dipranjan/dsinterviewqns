---
html_meta:
  "description lang=en": "Interview resource of Data Science Interview focusing on Excel basics."
  "keywords": "interview, Excel, practice questions"
  "property=og:locale": "en_US"
---

## Time and Date

```{warning}
This page is a work in progress
```

```{note}
Excel, as a product, always remains under active development from Microsoft. With new releases, new features are brought in whereas old ones are discarded. Due to this there might be changes to the solutions mentioned below depending on the version that you are using.
```

```{admonition} Problem: Add Month or Year
:class: tip, dropdown

In may cases you will get business problems where you need to add or subtract month/year from a given date. Can you show how to do that in excel?
```

```{admonition} Solution:
:class: dropdown
This can be done easily using the `DATE` function. The below formula will deduct a month, similarly one can change the year and date.

`
  =DATE(YEAR(A3),MONTH(A3)-1,DAY(A3))
`

```