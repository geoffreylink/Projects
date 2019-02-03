from pyspark.ml.feature import StopWordsRemover
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

sentenceData = spark.createDataFrame([
                                      (0, ["I", "saw", "the", "red", "balloon"]),
                                      (1, ["Mary", "had", "a", "little", "lamb"])
                                     ], ["id", "raw"])

remover = StopWordsRemover(inputCol="raw", outputCol="filtered")
remover.transform(sentenceData).show(truncate=False)

spark.stop()
