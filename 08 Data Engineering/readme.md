<p>Removal, Anonymization, Encryption, Tokenization, Differential Privacy</p>
<p>http://principlesofchaos.org</p>
<p>https://stedolan.github.io/jq/</p>
<p>ipecho.net</p>
<p>explainshell.com</p>
<p>nginx</p>
<p>flask</p>
<p>Rails(Ruby) App Server</p>
<p>Drupal</p>
<p>lsb_release -a</p>
<p>htop</p>
<p>tmux</p>
<p>ip -a</p>
<p>Thoughtworks -> Sadalage, Fowler, Kleppman</p>
<p>Netflix blog is likely the best to watch for Data Engineering</p>
<p>https://medium.com/netflix-techblog/evolution-of-the-netflix-data-pipeline-da246ca36905</p>
<p>https://medium.com/netflix-techblog/kafka-inside-keystone-pipeline-dd5aeabaf6bb</p>
<p>---</p>
<p>p402 of Spark: The Definitive Guide:</p>
<p>-</p>
<p>The most common tasks include:</p>
<p>- Preprocessing data (cleaning data and feature engineering)</p>
<p>- Supervised learning, including classification and regression, where the goal is to predict a label for each data point based on various features.</p>
<p>- Recommendation engines to suggest products to users based on behaviour.</p>
<p>- Unsupervised learning, including clustering, anomaly detection, and topic modelling, where the goal is to discover structure in the data.</p>
<p>- Graph analytics tasks such as searching for patterns in a social network.</p>
<p>- Deep Learning</p>
<p>- Frequent Pattern Mining</p>
<p>- Probablistic Modeling</p>
<p>---</p>
<p>p424 of Spark: The Definitive Guide:</p>
<p>-</p>
<p>Deployment Patterns:</p>
<p>- Offline data.  Not data that you need to get an answer from quickly.  Spark is well suited to this sort of deployment.  Persist the model to disk (not low latency, very high!)</p>
<p>- Database (usually a key-value store).  This works well for something like recommendation but poorly for something like classification or regression where you cannot just look up a value for a given user but must calculate one based on the input.</p>
<p>- PMML.  Convert distributed model to one that can run locally.</p>
<p>- Online data.  Structured Streaming - can be complex for some models.</p>
<p>---</p>
<p>p427 of Spark: The Definitive Guide:</p>
<p>-</p>
<p>Formating Models According to Your Use Case:</p>
<p>- In the case of most classification and regression algorithms, you want to get your data into a column of type Double to represent the label and a column of type Vector (either dense or sparse) to represent the features.</p>
<p>- In the case of recommendations, you want to get your data into a column of users, a column of items (say movies or books), and a column of ratings.</p>
<p>- In the case of unsupervised learning, a column of type Vector (either dense or sparse) is needed to represent the features.</p>
<p>- In the case of graph analytics, you will want a DataFrame of vertices and a DataFrame of edges.</p>
<p>---</p>
