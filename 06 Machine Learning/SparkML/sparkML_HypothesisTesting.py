from pyspark.sql import SparkSession
from pyspark.ml.linalg import Vectors
from pyspark.ml.stat import ChiSquareTest

spark = SparkSession.builder.getOrCreate()

data = [
        (0.0, Vectors.dense(0.5, 10.0)),
        (0.0, Vectors.dense(1.5, 20.0)),
        (1.0, Vectors.dense(1.5, 30.0)),
        (0.0, Vectors.dense(3.5, 30.0)),
        (0.0, Vectors.dense(3.5, 40.0)),
        (1.0, Vectors.dense(3.5, 40.0))
       ]

df = spark.createDataFrame(data, ["label", "features"])
r  = ChiSquareTest.test(df, "features", "label").head()

df.show()
print("pValues: " + str(r.pValues))
print("degreesOfFreedom: " + str(r.degreesOfFreedom))
print("statistics: " + str(r.statistics))

spark.stop()
