# Time and Date

{% hint style="warning" %}
This page is a Work in Progress
{% endhint %}

{% hint style="info" %}
Excel, as a product, always remains under active development from Microsoft. With new releases, new features are brought in whereas old ones are discarded. Due to this there might be changes to the solutions mentioned below depending on the version that you are using.
{% endhint %}

<details>

<summary>Time Diff</summary>

In many cases you will get business problems where you need to add or subtract month/year from a given date. Can you show how to do that in excel?

**Answer**

This can be done easily using the `DATE` function. The below formula will deduct a month, similarly one can change the year and date.

&#x20;`=DATE(YEAR(A3),MONTH(A3)-1,DAY(A3))`

</details>
