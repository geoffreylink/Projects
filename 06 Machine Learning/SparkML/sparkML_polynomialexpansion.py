from pyspark.ml.feature import PolynomialExpansion
from pyspark.ml.linalg import Vectors
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.createDataFrame([
                            (Vectors.dense([2.0, 1.0]),),
                            (Vectors.dense([0.0, 0.0]),),
                            (Vectors.dense([3.0, -1.0]),)
                           ], ["features"])

polyExpansion = PolynomialExpansion(degree=3, inputCol="features", outputCol="polyFeatures")
polyDF        = polyExpansion.transform(df)

polyDF.show(truncate=False)

spark.stop()
