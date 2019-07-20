from pyspark.sql import SparkSession
from pyspark.ml.stat import Summarizer
from pyspark.sql import Row
from pyspark.ml.linalg import Vectors

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

sc = spark.sparkContext

df = sc.parallelize([
                     Row(weight=1.0, features=Vectors.dense(1.0, 1.0, 1.0)),
                     Row(weight=0.0, features=Vectors.dense(1.0, 2.0, 3.0))
                    ]).toDF()

summarizer = Summarizer.metrics("mean", "count")

df.show()
df.select(summarizer.summary(df.features, df.weight)).show(truncate=False)
df.select(summarizer.summary(df.features)).show(truncate=False)
df.select(Summarizer.mean(df.features, df.weight)).show(truncate=False)
df.select(Summarizer.mean(df.features)).show(truncate=False)

spark.stop()
