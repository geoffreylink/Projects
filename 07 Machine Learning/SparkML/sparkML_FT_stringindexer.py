from pyspark.ml.feature import StringIndexer
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.createDataFrame(
                           [
                            (0, "a"),
                            (1, "b"),
                            (2, "c"),
                            (3, "a"),
                            (4, "a"),
                            (5, "c")
                           ],
                           ["id", "category"]
                          )

indexer = StringIndexer(inputCol="category", outputCol="categoryIndex")
indexed = indexer.fit(df).transform(df)
indexed.show()

spark.stop()
