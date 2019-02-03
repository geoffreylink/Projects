from pyspark.ml.feature import SQLTransformer
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.createDataFrame([
                            (0, 1.0, 3.0),
                            (2, 2.0, 5.0)
                           ], ["id", "v1", "v2"])

sqlTrans = SQLTransformer(statement="SELECT *, (v1 + v2) AS v3, (v1 * v2) AS v4 FROM __THIS__")
sqlTrans.transform(df).show()

spark.stop()
