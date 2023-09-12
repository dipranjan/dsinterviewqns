---
description: >-
  This page broadly summarizes the steps needed to go from data gathering to
  model building
---

# Overview

1. Gather the data
2. Import and understand the data: do things like the following to understand more about the data at hand
   1. check the shape of data
   2. check the number of unique values in each column, drop the ones which have the same value
   3. if it is a classification problem check for class imbalance
   4. check for column datatypes and fix if necessary
3. Check and fix for missing values: [Read more about this here](data/missing-value.md)
4. Perform feature engineering to build new columns from the existing ones, it can be YoY growth, etc.
5. Run univariate and multivariate analysis to understand more about the features
6. Detect and treat outliers: [Read more about this here](data/outlier.md)
7. Encode categorical variables: [Read more about this here](data/categorical-variable.md)
8. Standardize the data
9. If needed run different sampling techniques to reduce imbalance or run PCA etc.
10. Split the data to train, test and validation
11. Determine on the metric to track
12. Run some basic algorithms to understand which models might give the best results, PYCARET   is a good option to quickly prototype
13. Select the promising ones and deep dive on those
14. Check if there are any assumptions of the model --> Perform checks on Collinearity etc.
15. [Tune the model ](hyperparameter-optimization.md)--> Use regularization, Cross validation etc. to reduce overfitting
16. Check for feature importance using built in functions or SHAP



