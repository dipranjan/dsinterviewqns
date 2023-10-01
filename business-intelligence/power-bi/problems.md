# Problems

<details>

<summary>Calculated Column vs Measure</summary>

Can you explain the difference between Calculated Column vs Measure?

**Answer**

A calculated column belongs to a single table, while a measure belongs to the whole data model. A calculated column is evaluated in a row context (row by row, like in an excel table), while a measure is evaluated in the filter context.

Measures result in lower file size compared to calculated columns.

</details>

<details>

<summary>Difference in Direct Query and Importing data in PowerBI</summary>

Can you explain the difference between Direct Query and Importing the data in Power BI?

**Answer**

When using the Direct Query method of connection, your dashboard will be directly querying the data source at run time. Every filter and interaction with the report will kick off further queries. No data is imported into Power BI so you are always querying the data that is present in the data source itself.

The Import method of connection means that Power BI will cache the data that you’re connected to creating a point in time snapshot of your data. All of the interactions and filters applied to your data will be done to this compressed cache source instead of the actual data source itself.&#x20;

Advantages of using Power BI Direct Query:

* Data is queried from the data source so you are getting the most up to date data. The report refreshes occur every 15 minutes.

<!---->

* Since you are not caching your data when using Direct Query, your Power BI Desktop files are much smaller and easier to work with (faster saving, publishing etc.)

Disadvantages of using Power BI Direct Query:

* Because you’re querying the data source at run time, you might be competing with other users for bandwidth. You’re also not taking advantage of the compression of the Vertipaq performance engine.

<!---->

* You are not able to use all of the normal Power Query transformation features. Particular DAX functions are not available in this method as well. So if your data is poorly structured or needing lots of transformation, sometimes Direct Query is not a viable option.

Advantages of using Power BI Import:

* When you cache your data you are able to take full advantage of the Vertipaq performance engine. Normally your report performance will be better using this method.

<!---->

* Unlike in Direct Query, you are able to use all M and DAX functions (notably all time intelligence functions), format fields however you desire, and there are no limitations to data modeling.

<!---->

* Using Import you are able to combine data sources from various data sources (data flows, databases, csv).

Disadvantages of using Power BI Import:

* You can schedule up to 8 refreshes a day ([Premium SKUs](https://www.phdata.io/blog/what-is-the-price-of-power-bi-premium-and-what-sku-should-you-choose/) allow more), but you also need to consider the amount of reports you’re maintaining and how big the data sets are that you’re refreshing.

<!---->

* Import caches are limited to 1GB per dataset (can be increased in Premium). While the Vertipaq engine does a great job a compression, you will still need to consider this when choosing your connection method
* Crazy enough, once you’ve selected Import, you cannot switch back to using Direct Query. So make sure you want Import before making the switch, or else you’ll have more work ahead of you!

</details>
