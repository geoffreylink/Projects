from pyspark.ml.feature import MaxAbsScaler
from pyspark.ml.linalg import Vectors
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

dataFrame = spark.createDataFrame([
                                   (0, Vectors.dense([1.0, 0.1, -8.0]),),
                                   (1, Vectors.dense([2.0, 1.0, -4.0]),),
                                   (2, Vectors.dense([4.0, 10.0, 8.0]),)
                                  ], ["id", "features"])

scaler      = MaxAbsScaler(inputCol="features", outputCol="scaledFeatures")
scalerModel = scaler.fit(dataFrame)
scaledData  = scalerModel.transform(dataFrame)
scaledData.select("features", "scaledFeatures").show()

spark.stop()
