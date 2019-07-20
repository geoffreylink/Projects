from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

dataset = spark.read.format("libsvm").load("file:///usr/lib/spark/data/mllib/sample_kmeans_data.txt")

kmeans = KMeans().setK(2).setSeed(1)
model  = kmeans.fit(dataset)

predictions = model.transform(dataset)
evaluator   = ClusteringEvaluator()

silhouette = evaluator.evaluate(predictions)
print("Silhouette with squared euclidean distance = " + str(silhouette))

centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
  print(center)

spark.stop()
