from pyspark.ml.feature import StandardScaler
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

dataFrame   = spark.read.format("libsvm").load("file:///usr/lib/spark/data/mllib/sample_libsvm_data.txt")

scaler      = StandardScaler(inputCol="features", outputCol="scaledFeatures",withStd=True, withMean=False)
scalerModel = scaler.fit(dataFrame)

scaledData = scalerModel.transform(dataFrame)
scaledData.show()

spark.stop()
