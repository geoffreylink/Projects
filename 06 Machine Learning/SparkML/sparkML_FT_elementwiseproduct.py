from pyspark.ml.feature import ElementwiseProduct
from pyspark.ml.linalg import Vectors
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

data = [
        (Vectors.dense([1.0, 2.0, 3.0]),),
        (Vectors.dense([4.0, 5.0, 6.0]),)
       ]

df = spark.createDataFrame(data, ["vector"])

transformer = ElementwiseProduct(scalingVec=Vectors.dense([0.0, 1.0, 2.0]),inputCol="vector", outputCol="transformedVector")
transformer.transform(df).show()

spark.stop()
