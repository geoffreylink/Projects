from pyspark.ml.feature import Imputer
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.createDataFrame([
                            (1.0, float("nan")),
                            (2.0, float("nan")),
                            (float("nan"), 3.0),
                            (4.0, 4.0),
                            (5.0, 5.0)
                           ], ["a", "b"])

imputer = Imputer(inputCols=["a", "b"], outputCols=["out_a", "out_b"])
model   = imputer.fit(df)
model.transform(df).show()

spark.stop()
