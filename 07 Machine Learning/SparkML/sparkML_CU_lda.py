from pyspark.ml.clustering import LDA
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

dataset = spark.read.format("libsvm").load("file:///usr/lib/spark/data/mllib/sample_lda_libsvm_data.txt")

lda   = LDA(k=10, maxIter=10)
model = lda.fit(dataset)

ll = model.logLikelihood(dataset)
lp = model.logPerplexity(dataset)
print("The lower bound on the log likelihood of the entire corpus: " + str(ll))
print("The upper bound on perplexity: " + str(lp))

topics = model.describeTopics(3)
print("The topics described by their top-weighted terms:")
topics.show(truncate=False)

transformed = model.transform(dataset)
transformed.show(truncate=False)

spark.stop()
