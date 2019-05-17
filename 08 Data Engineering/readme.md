## Reference

* [pythex](https://pythex.org)
* [Awesome Python](https://awesome-python.com)
* [PySpark Cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PySpark_Cheat_Sheet_Python.pdf)
* [Scikit-Learn Pipeline Examples](http://queirozf.com/entries/scikit-learn-pipeline-examples)
* [Kafka Inside Keystone Pipeline](https://medium.com/netflix-techblog/kafka-inside-keystone-pipeline-dd5aeabaf6bb)
* [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org)
* [Evolution of the Netflix Data Pipeline](https://medium.com/netflix-techblog/evolution-of-the-netflix-data-pipeline-da246ca36905)
* [Auto-scaling scikit-learn with Apache Spark](https://databricks.com/blog/2016/02/08/auto-scaling-scikit-learn-with-apache-spark.html)
* [Ever Wonder How Spotify Discover Weekly Works?](http://blog.galvanize.com/spotify-discover-weekly-data-science/)
* [Why Are There So Many Pythons? A Python Implementation Comparison](https://www.toptal.com/python/why-are-there-so-many-pythons)
* [Buggy Python Code: The 10 Most Common Mistakes That Python Developers Make](https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make)

## Privacy

* Removal
* Encryption
* Tokenization
* Anonymization
* Differential Privacy

## Spark

* Deep Learning
* Fraud Detection
* Anomaly Detection
* Pattern Recognition
* Probablistic Modeling
* Prediction (IoT & NLP)
* Frequent Pattern Mining
* Predictive Maintenance
* Preprocessing data (cleaning data and feature engineering)
* Recommendation engines to suggest products to users based on behaviour
* Graph analytics tasks such as searching for patterns in a social network
* Unsupervised learning, including clustering, anomaly detection, and topic modelling, where the goal is to discover structure in the data
* Supervised learning, including classification and regression, where the goal is to predict a label for each data point based on various features

## Deployment

* [PMML](https://en.wikipedia.org/wiki/Predictive_Model_Markup_Language).  Convert distributed model to one that can run locally
* Online data.  Structured Streaming - can be complex for some models
* Offline data.  Not data that you need to get an answer from quickly.  Spark is well suited to this sort of deployment.  Persist the model to disk (not low latency, very high!)
* Database (usually a key-value store).  This works well for something like recommendation but poorly for something like classification or regression where you cannot just look up a value for a given user but must calculate one based on the input

## Format

* In the case of graph analytics, you will want a DataFrame of vertices and a DataFrame of edges
* In the case of unsupervised learning, a column of type Vector (either dense or sparse) is needed to represent the features
* In the case of recommendations, you want to get your data into a column of users, a column of items (say movies or books), and a column of ratings
* In the case of most classification and regression algorithms, you want to get your data into a column of type Double to represent the label and a column of type Vector (either dense or sparse) to represent the features

![](https://github.com/geoffreylink/Projects/blob/master/08%20Data%20Engineering/images/CloudInfrastructureMarketShare.png)

## Cloud Computing Patterns & Variants

![](https://github.com/geoffreylink/Projects/blob/master/08%20Data%20Engineering/images/CloudComputingPatterns.png)
![](https://github.com/geoffreylink/Projects/blob/master/08%20Data%20Engineering/images/CloudComputingVariants.png)

## Visual Guide to Data Engineering

![](https://github.com/geoffreylink/Projects/blob/master/08%20Data%20Engineering/images/DataEngineering.png)

## Data Pipeline

![](https://github.com/geoffreylink/Projects/blob/master/08%20Data%20Engineering/images/HighLevel_Pipeline.png)

## Layering with Kafka

![](https://github.com/geoffreylink/Projects/blob/master/08%20Data%20Engineering/images/Layering_Kafka.png)

## Spark Streaming

![](https://github.com/geoffreylink/Projects/blob/master/08%20Data%20Engineering/images/Streaming_Spark.png)

## Netflix Streaming

![](https://github.com/geoffreylink/Projects/blob/master/08%20Data%20Engineering/images/Streaming_Netflix.png)

## Spotify Discover Weekly

![](https://github.com/geoffreylink/Projects/blob/master/08%20Data%20Engineering/images/SpotifyDiscoverWeekly.png)


## Graphana Monitoring

![](https://github.com/geoffreylink/Projects/blob/master/08%20Data%20Engineering/images/Graphana_Kafka.png)
