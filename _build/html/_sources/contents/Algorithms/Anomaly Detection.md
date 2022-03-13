---
html_meta:
  "description lang=en": "Interview resource of Data Science focusing on Anomaly Detection."
  "keywords": "interview, data science, machine learning, Anomaly Detection, Isolation Forest"
  "property=og:locale": "en_US"
---

## Anomaly Detection

### Questions

```{admonition} Problem: [AKAMAI] Anomaly in Univariate Dataset
:class: tip, dropdown

**Asked By - AKAMAI**

If given a univariate dataset, how would you design a function to detect anomalies?

What if the data is bivariate?
```

```{admonition} Solution:
:class: dropdown
**Reference:** [📖Explanation](https://towardsdatascience.com/anomaly-detection-for-dummies-15f148e559c1)

Anomaly detection is the process of identifying unexpected items or events in data sets, which differ from the norm. And anomaly detection is often applied on unlabeled data which is known as unsupervised anomaly detection. Anomaly detection has two basic assumptions:
- Anomalies only occur very rarely in the data.
- Their features differ from the normal instances significantly.

For Univariate Analysis Isolation Forest can be used to detect outliers that returns the anomaly score of each sample. Isolation Forest is a tree-based model. In these trees, partitions are created by first randomly selecting a feature and then selecting a random split value between the minimum and maximum value of the selected feature.

In multivariate anomaly detection, outlier is a combined unusual score on at least two variables. For Multivariate Analysis multiple options are avaliable other than isolation forest:

- The Cluster-based Local Outlier Factor (CBLOF) calculates the outlier score based on cluster-based local outlier factor. An anomaly score is computed by the distance of each instance to its cluster center multiplied by the instances belonging to its cluster.

- Histogram-based Outlier Detection (HBOS) assumes the feature independence and calculates the degree of anomalies by building histograms. In multivariate anomaly detection, a histogram for each single feature can be computed, scored individually and combined at the end.

- KNN is one of the simplest methods in anomaly detection. For a data point, its distance to its kth nearest neighbor could be viewed as the outlier score.

An ensemble of these methods can be used to finalize the anamolies. Always visually investigate some of the anomalies.

```