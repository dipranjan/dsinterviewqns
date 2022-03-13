---
html_meta:
  "description lang=en": "Interview resource of Data Science Interview focusing on Data Scaling."
  "keywords": "interview, data science, machine learning, Scaling, Data Normalization"
  "property=og:locale": "en_US"
---

## Scaling

**Feature scaling is a method used to standardize the range of independent variables or features of data. In data processing, it is also known as data normalization and is generally performed during the data preprocessing step.**

Since the range of values of raw data varies widely, in some machine learning algorithms, objective functions will not work properly without normalization. For example, the majority of classifiers calculate the distance between two points by the Euclidean distance. If one of the features has a broad range of values, the distance will be governed by this particular feature. Therefore, the range of all features should be normalized so that each feature contributes approximately proportionately to the final distance. 
Another reason why feature scaling is applied is that gradient descent converges much faster with feature scaling than without it.

### Rescaling (min-max normalization)

Also known as min-max scaling or min-max normalization, is the simplest method and consists in rescaling the range of features to scale the range in $[0, 1]$ or $[−1, 1]$. Selecting the target range depends on the nature of the data. The general formula is given as: 

$x^{\prime} = \frac{x - min(x)}{max(x) - min(x)}$

### Mean normalization

This is similar to above with a slight change:
$x^{\prime} = \frac{x - average(x)}{max(x) - min(x)}$

### Standardization

In machine learning, we can handle various types of data, e.g. audio signals and pixel values for image data, and this data can include multiple dimensions. Feature standardization makes the values of each feature in the data have zero-mean (when subtracting the mean in the numerator) and unit-variance. This method is widely used for normalization in many machine learning algorithms (e.g., support vector machines, logistic regression, and artificial neural networks).

$x^{\prime} = \frac{x - \bar x}{\sigma}$

### Scaling to Unit length

Another option that is widely used in machine-learning is to scale the components of a feature vector such that the complete vector has length one. This usually means dividing each component by the Euclidean length of the vector:

$x^{\prime} = \frac{x}{\Vert x \Vert}$

In some applications (e.g. Histogram features) it can be more practical to use the L1 norm (i.e. Manhattan Distance, City-Block Length or Taxicab Geometry) of the feature vector. This is especially important if in the following learning steps the Scalar Metric is used as a distance measure. 
