from pyspark.ml.feature import VectorIndexer
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

data                = spark.read.format("libsvm").load("file:///usr/lib/spark/data/mllib/sample_libsvm_data.txt")
indexer             = VectorIndexer(inputCol="features", outputCol="indexed", maxCategories=10)
indexerModel        = indexer.fit(data)
categoricalFeatures = indexerModel.categoryMaps

print("Chose %d categorical features: %s" % (len(categoricalFeatures), ", ".join(str(k) for k in categoricalFeatures.keys())))
indexedData = indexerModel.transform(data)
indexedData.show()

spark.stop()
