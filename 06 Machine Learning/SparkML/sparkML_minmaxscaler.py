from pyspark.ml.feature import MinMaxScaler
from pyspark.ml.linalg import Vectors
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

dataFrame = spark.createDataFrame([
                                   (0, Vectors.dense([1.0, 0.1, -1.0]),),
                                   (1, Vectors.dense([2.0, 1.1, 1.0]),),
                                   (2, Vectors.dense([3.0, 10.1, 3.0]),)
                                  ], ["id", "features"])

scaler      = MinMaxScaler(inputCol="features", outputCol="scaledFeatures")
scalerModel = scaler.fit(dataFrame)
scaledData  = scalerModel.transform(dataFrame)

print("Features scaled to range: [%f, %f]" % (scaler.getMin(), scaler.getMax()))
scaledData.select("features", "scaledFeatures").show()

spark.stop()
