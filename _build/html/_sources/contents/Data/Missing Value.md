---
html_meta:
  "description lang=en": "Interview resource of Data Science Interview focusing on Missing value treatment."
  "keywords": "interview, data science, machine learning, Missing value"
  "property=og:locale": "en_US"
---

## Missing Value

[📖Source](https://www.analyticsvidhya.com/blog/2016/01/guide-data-exploration/)

Data can have missing values and it is very common. The reason of such missing data can be any of the following:

- **Data Extraction:** It is possible that there are problems with extraction process. In such cases, we should double-check for correct data with data guardians.
- **Data collection:** These errors occur at time of data collection and are harder to correct. They can be categorized in four types:
	- **Missing completely at random:** This is a case when the probability of missing variable is same for all observations
	- **Missing at random:** This is a case when variable is missing at random and missing ratio varies for different values / level of other input variables. For example: We are collecting data for age and female has higher missing value compare to male.
	- **Missing that depends on unobserved predictors:** This is a case when the missing values are not random and are related to the unobserved input variable. For example: In a medical study, if a particular diagnostic causes discomfort, then there is higher chance of drop out from the study. This missing value is not at random unless we have included “discomfort” as an input variable for all patients.
	- **Missing that depends on the missing value itself:** This is a case when the probability of missing value is directly correlated with missing value itself. For example: People with higher or lower income are likely to provide non-response to their earning.

There are many standard practices of dealing with missing data-

- **Deletion:**  It is of two types: *List Wise Deletion* and *Pair Wise Deletion*.
In list wise deletion, we delete observations where any of the variable is missing. Simplicity is one of the major advantage of this method, but this method reduces the power of model because it reduces the sample size.
In pair wise deletion, we perform analysis with all cases in which the variables of interest are present. Advantage of this method is, it keeps as many cases available for analysis. One of the disadvantage of this method, it uses different sample size for different variables.

**Deletion methods are used when the nature of missing data is “Missing completely at random” else non random missing values can bias the model output.**

- **Mean/ Mode/ Median Imputation:** Imputation is a method to fill in the missing values with estimated ones. The objective is to employ known relationships that can be identified in the valid values of the data set to assist in estimating the missing values. Mean/Mode/Median imputation is one of the most frequently used methods. It consists of replacing the missing data for a given attribute by the mean or median (quantitative attribute) or mode (qualitative attribute) of all known values of that variable. It can be of two types:-
	- **Generalized Imputation:** In this case, we calculate the mean or median for all non missing values of that variable then replace missing value with mean or median.
	- **Similar case Imputation:** In this case, for example, we calculate average for gender “Male” (29.75) and “Female” (25) individually of non missing values then replace the missing value based on gender. For “Male“, we will replace missing values of manpower with 29.75 and for “Female” with 25.

- **Prediction Model:**  Prediction model is one of the sophisticated method for handling missing data. Here, we create a predictive model to estimate values that will substitute the missing data.  In this case, we divide our data set into two sets: One set with no missing values for the variable and another one with missing values. First data set become training data set of the model while second data set with missing values is test data set and variable with missing values is treated as target variable. Next, we create a model to predict target variable based on other attributes of the training data set and populate missing values of test data set.We can use regression, ANOVA, Logistic regression and various modeling technique to perform this. There are 2 drawbacks for this approach:
	- The model estimated values are usually more well-behaved than the true values
	- If there are no relationships with attributes in the data set and the attribute with missing values, then the model will not be precise for estimating missing values

- **KNN Imputation:** In this method of imputation, the missing values of an attribute are imputed using the given number of attributes that are most similar to the attribute whose values are missing. The similarity of two attributes is determined using a distance function.

	**Advantages:**
	- k-nearest neighbour can predict both qualitative & quantitative attributes
	- Creation of predictive model for each attribute with missing data is not required
	- Attributes with multiple missing values can be easily treated
	- Correlation structure of the data is taken into consideration
	
	**Disadvantage:**
	- KNN algorithm is very time-consuming in analyzing large database. It searches through all the dataset looking for the most similar instances.
	- Choice of k-value is very critical. Higher value of k would include attributes which are significantly different from what we need whereas lower value of k implies missing out of significant attributes.