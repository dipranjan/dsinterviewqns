# Feature Store

Many machine learning and AI models work best on summaries of raw data called _features_. These features structure information into a form that makes it easier to train algorithms.

A simple feature might involve transforming a raw date into a weekday or weekend, both of which might be better predictors of behavior than a raw date number. Other kinds of features can be more complex and require intricate calculations across many data streams. A feature store provides a place to organize the most popular features so they can be reused across projects rather than redone from scratch every time they're used.

A feature store can increase automation, improve productivity by promoting sharing and reuse, reduce technical debt in software code, ensure consistency in calculations and provide governance, auditability and lineage for regulatory compliance, according to David Sweenor, senior director of product marketing at data science tools company Alteryx. However, a feature store isn't ideal for every company. Smaller ones may struggle with the overhead required to create and maintain a feature store. Companies may also struggle with reusing features across departments.

### What are the benefits of a feature store?

A feature, as it relates to data science, is any variable that can be used for analytics. Simple examples include name, age, sex, zip code and amount. These raw variables are transformed through a process known as _feature engineering_ to yield better predictions. For example, a date could be transformed into a day of the week, a day of the year or a holiday.

A feature store enables a data scientist to create this transformation once rather than having each data scientist recreate the same features repeatedly. This ensures consistency since everyone is using the exact same transformation as part of their models. It also reduces the need to insert the same algorithm within code. If a company decides to change a complex feature, a feature store enables them to change it once and propagate it across all models that use it. Otherwise, someone would have to manually edit all the models using that feature.

Since processing these data is very expensive, and these data are slow-changing, it makes sense to process them once every hour or day and store the features into a feature store for hundreds of teams to use \[machine learning] ML to solve their business problems.
