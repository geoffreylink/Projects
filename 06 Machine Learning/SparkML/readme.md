# AWS EMR

* 1 m1.large spot instance max $0.02/hr (10 minute start)

# Spark MLlib
  
* [Spark MLlib 2.4.0](https://spark.apache.org/docs/latest/ml-guide.html)
* BASIC = Basic Functionality
* CF = Collaborative Filtering
* CL = Classification
* CU = Clustering
* FE = Feature Extractors
* FP = Frequent Pattern
* FS = Feature Selector
* FT = Feature Transformers
* PIPE = Pipeline Construction
* RG = Regression
* TU = Tuning

# Common Use cases

* Deep Learning
* Probablistic Modeling
* Frequent Pattern Mining
* Preprocessing data: cleaning data and feature engineering
* Graph analytics tasks such as searching for patterns in a social network
* Recommendation engines to suggest products to users based upon behaviour
* Supervised learning including classification and regression, where the goal is to predict a label for each data point based on various features
* Unsupervised learning including clustering, anomaly detection, and topic modelling, where the goal is to discover structure in the data

# Deployment Patterns

* PMML.  Convert distributed model to one that can run locally.
* Online data.  Structured Streaming - can be complex for some models.
* Offline data.  Not data that you need to get an answer from quickly.  Spark is well suited to this sort of deployment.  Persist the model to disk (not low latency, very high!)
* Database (usually a key-value store).  This works well for something like recommendation but poorly for something like classification or regression where you cannot just look up a value for a given user but must calculate one based on the input.
