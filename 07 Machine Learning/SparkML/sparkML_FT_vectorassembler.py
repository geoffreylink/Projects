from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

dataset   = spark.createDataFrame(
                                  [(0, 18, 1.0, Vectors.dense([0.0, 10.0, 0.5]), 1.0)],
                                  ["id", "hour", "mobile", "userFeatures", "clicked"]
                                 )

assembler = VectorAssembler(
                            inputCols=["hour", "mobile", "userFeatures"],
                            outputCol="features"
                           )

output    = assembler.transform(dataset)
print("Assembled columns 'hour', 'mobile', 'userFeatures' to vector column 'features'")
output.select("features", "clicked").show(truncate=False)

spark.stop()
