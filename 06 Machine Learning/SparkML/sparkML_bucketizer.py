from pyspark.sql import SparkSession
from pyspark.ml.feature import Bucketizer

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

splits    = [-float("inf"), -0.5, 0.0, 0.5, float("inf")]
data      = [(-999.9,), (-0.5,), (-0.3,), (0.0,), (0.2,), (999.9,)]
dataFrame = spark.createDataFrame(data, ["features"])

bucketizer   = Bucketizer(splits=splits, inputCol="features", outputCol="bucketedFeatures")
bucketedData = bucketizer.transform(dataFrame)

print("Bucketizer output with %d buckets" % (len(bucketizer.getSplits())-1))
bucketedData.show()

spark.stop()
