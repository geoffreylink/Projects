## Reference
* [Dask](https://dask.org)
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
* [pythex](https://pythex.org)
* [Numba](https://numba.pydata.org)
* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
* [Awesome Python](https://awesome-python.com)
* [Imbalanced-Learn](http://imbalanced-learn.org/en/stable/index.html)
* [PySpark Cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PySpark_Cheat_Sheet_Python.pdf)
* [Scikit-Learn Pipeline Examples](http://queirozf.com/entries/scikit-learn-pipeline-examples)
* [Kafka Inside Keystone Pipeline](https://medium.com/netflix-techblog/kafka-inside-keystone-pipeline-dd5aeabaf6bb)
* [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org)
* [Data Modeling in AWS DynamoDB](https://medium.com/swlh/data-modeling-in-aws-dynamodb-dcec6798e955)
* [Structured Streaming with PySpark](https://hackingandslacking.com/structured-streaming-with-pyspark-9355f792897a)
* [Evolution of the Netflix Data Pipeline](https://medium.com/netflix-techblog/evolution-of-the-netflix-data-pipeline-da246ca36905)
* [9 Amazing Articles on Python Programming](https://medium.com/better-programming/10-great-articles-on-python-development-6f54dd38437f)
* [An Overview of Python’s Datatable package](https://towardsdatascience.com/an-overview-of-pythons-datatable-package-5d3a97394ee9)
* [Auto-scaling scikit-learn with Apache Spark](https://databricks.com/blog/2016/02/08/auto-scaling-scikit-learn-with-apache-spark.html)
* [A Technical Analysis of the Capital One Hack](https://blog.cloudsploit.com/a-technical-analysis-of-the-capital-one-hack-a9b43d7c8aea)
* [Time Complexities Of Python Data Structures](https://medium.com/fintechexplained/time-complexities-of-python-data-structures-ddb7503790ef)
* [3 Great Additions for your Jupyter Notebooks](https://towardsdatascience.com/three-great-additions-for-your-jupyter-notebooks-cd7373b00e96)
* [Ever Wonder How Spotify Discover Weekly Works?](http://blog.galvanize.com/spotify-discover-weekly-data-science/)
* [GPU Accelerated Data Analytics & Machine Learning](https://towardsdatascience.com/gpu-accelerated-data-analytics-machine-learning-963aebe956ce)
* [Once You’re in the Cloud, How Expensive Is It to Get Out?](https://www.nefiber.com/blog/cloud-egress-charges/)
* [Use Cython to get more than 30X speedup on your Python code](https://towardsdatascience.com/use-cython-to-get-more-than-30x-speedup-on-your-python-code-f6cb337919b6)
* [One Simple Trick for Speeding up your Python Code with Numpy](https://towardsdatascience.com/one-simple-trick-for-speeding-up-your-python-code-with-numpy-1afc846db418)
* [Everything a Data Scientist Should Know About Data Management](https://towardsdatascience.com/everything-a-data-scientist-should-know-about-data-management-6877788c6a42)
* [Python Pro Tip: Use Itertools, Generators, and Generator Expressions](https://towardsdatascience.com/python-pro-tip-use-itertools-generators-and-generator-expressions-1b84911c978)
* [Why Are There So Many Pythons? A Python Implementation Comparison](https://www.toptal.com/python/why-are-there-so-many-pythons)
* [From relational DB to single DynamoDB table: a step-by-step exploration](https://www.trek10.com/blog/dynamodb-single-table-relational-modeling/)
* [Here’s how you can get some free speed on your Python code with Numba](https://towardsdatascience.com/heres-how-you-can-get-some-free-speed-on-your-python-code-with-numba-89fdc8249ef3)
* [The Why, When, and How of Using Python Multi-threading and Multi-Processing](https://medium.com/towards-artificial-intelligence/the-why-when-and-how-of-using-python-multi-threading-and-multi-processing-afd1b8a8ecca)
* [Buggy Python Code: The 10 Most Common Mistakes That Python Developers Make](https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make)
* [Call an Amazon SageMaker model endpoint using Amazon API Gateway and AWS Lambda](https://aws.amazon.com/blogs/machine-learning/call-an-amazon-sagemaker-model-endpoint-using-amazon-api-gateway-and-aws-lambda/?ref=Welcome.AI)


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

## Pandas, Dask, PySpark
![](https://github.com/geoffreylink/Projects/blob/master/09%20Data%20Engineering/images/PandasDaskPySpark.png)

## Data Processing Evolution
![](https://github.com/geoffreylink/Projects/blob/master/09%20Data%20Engineering/images/DataProcessingEvolution.png)

![](https://github.com/geoffreylink/Projects/blob/master/09%20Data%20Engineering/images/CloudInfrastructureMarketShare.png)

## Containerization
![](https://github.com/geoffreylink/Projects/blob/master/09%20Data%20Engineering/images/Containerization.png)

## Cloud Computing Patterns & Variants
![](https://github.com/geoffreylink/Projects/blob/master/09%20Data%20Engineering/images/CloudComputingPatterns.png)
![](https://github.com/geoffreylink/Projects/blob/master/09%20Data%20Engineering/images/CloudComputingVariants.png)
![](https://github.com/geoffreylink/Projects/blob/master/09%20Data%20Engineering/images/CloudServices.png)

## Visual Guide to Data Engineering
![](https://github.com/geoffreylink/Projects/blob/master/09%20Data%20Engineering/images/DataManagement.jpeg)
![](https://github.com/geoffreylink/Projects/blob/master/09%20Data%20Engineering/images/DataEngineering.png)

## Data Pipeline
![](https://github.com/geoffreylink/Projects/blob/master/09%20Data%20Engineering/images/HighLevel_Pipeline.png)

## Layering with Kafka
![](https://github.com/geoffreylink/Projects/blob/master/09%20Data%20Engineering/images/Layering_Kafka.png)

## Spark Streaming
![](https://github.com/geoffreylink/Projects/blob/master/09%20Data%20Engineering/images/Streaming_Spark.png)

## Netflix
![](https://github.com/geoffreylink/Projects/blob/master/09%20Data%20Engineering/images/Streaming_Netflix.png)

## Spotify
![](https://github.com/geoffreylink/Projects/blob/master/09%20Data%20Engineering/images/SpotifyDiscoverWeekly.png)

## Graphana
![](https://github.com/geoffreylink/Projects/blob/master/09%20Data%20Engineering/images/Graphana_Kafka.png)

## AWS Sagemaker Endpoints
* [AWS Sagemaker Endpoints](https://youtu.be/KFuc2KWrTHs?list=PLhr1KZpdzukcOr_6j_zmSrvYnLUtgqsZz)
![](https://github.com/geoffreylink/Projects/blob/master/09%20Data%20Engineering/images/AWSSagemakerEndpoints.png)
