from pyspark.ml.clustering import GaussianMixture
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

dataset = spark.read.format("libsvm").load("file:///usr/lib/spark/data/mllib/sample_kmeans_data.txt")

gmm   = GaussianMixture().setK(2).setSeed(538009335)
model = gmm.fit(dataset)

print("Gaussians shown as a DataFrame: ")
model.gaussiansDF.show(truncate=False)

spark.stop()
