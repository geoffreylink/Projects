from pyspark.ml.feature import OneHotEncoderEstimator
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.createDataFrame([
                            (0.0, 1.0),
                            (1.0, 0.0),
                            (2.0, 1.0),
                            (0.0, 2.0),
                            (0.0, 1.0),
                            (2.0, 0.0)
                           ], ["categoryIndex1", "categoryIndex2"])

encoder = OneHotEncoderEstimator(
                                 inputCols=["categoryIndex1", "categoryIndex2"],
                                 outputCols=["categoryVec1", "categoryVec2"]
                                )

model   = encoder.fit(df)
encoded = model.transform(df)
encoded.show()

spark.stop()
