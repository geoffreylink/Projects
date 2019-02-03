from pyspark.ml.feature import QuantileDiscretizer
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

data = [(0, 18.0), (1, 19.0), (2, 8.0), (3, 5.0), (4, 2.2)]
df   = spark.createDataFrame(data, ["id", "hour"])

# Output of QuantileDiscretizer for such small datasets can depend on the number of
# partitions. Here we force a single partition to ensure consistent results.
# Note this is not necessary for normal use cases
df   = df.repartition(1)

discretizer = QuantileDiscretizer(numBuckets=3, inputCol="hour", outputCol="result")
result      = discretizer.fit(df).transform(df)
result.show()

spark.stop()
