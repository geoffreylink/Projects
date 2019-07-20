from pyspark.ml.clustering import BisectingKMeans
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

dataset = spark.read.format("libsvm").load("file:///usr/lib/spark/data/mllib/sample_kmeans_data.txt")

bkm   = BisectingKMeans().setK(2).setSeed(1)
model = bkm.fit(dataset)

cost = model.computeCost(dataset)
print("Within Set Sum of Squared Errors = " + str(cost))

print("Cluster Centers: ")
centers = model.clusterCenters()
for center in centers:
  print(center)

spark.stop()
