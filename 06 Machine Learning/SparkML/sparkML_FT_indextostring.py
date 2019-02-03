from pyspark.ml.feature import IndexToString, StringIndexer
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
model   = indexer.fit(df)
indexed = model.transform(df)
print("Transformed string column '%s' to indexed column '%s'" % (indexer.getInputCol(), indexer.getOutputCol()))
indexed.show()

converter = IndexToString(inputCol="categoryIndex", outputCol="originalCategory")
converted = converter.transform(indexed)
print("Transformed indexed column '%s' back to original string column '%s' using labels in metadata" % (converter.getInputCol(), converter.getOutputCol()))
converted.select("id", "categoryIndex", "originalCategory").show()

spark.stop()
