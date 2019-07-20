from pyspark.ml.feature import MinHashLSH
from pyspark.ml.linalg import Vectors
from pyspark.sql.functions import col
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

dataA = [(0, Vectors.sparse(6, [0, 1, 2], [1.0, 1.0, 1.0]),),
         (1, Vectors.sparse(6, [2, 3, 4], [1.0, 1.0, 1.0]),),
         (2, Vectors.sparse(6, [0, 2, 4], [1.0, 1.0, 1.0]),)]

dfA = spark.createDataFrame(dataA, ["id", "features"])

dataB = [(3, Vectors.sparse(6, [1, 3, 5], [1.0, 1.0, 1.0]),),
         (4, Vectors.sparse(6, [2, 3, 5], [1.0, 1.0, 1.0]),),
         (5, Vectors.sparse(6, [1, 2, 4], [1.0, 1.0, 1.0]),)]

dfB = spark.createDataFrame(dataB, ["id", "features"])

key = Vectors.sparse(6, [1, 3], [1.0, 1.0])

mh = MinHashLSH(inputCol="features", outputCol="hashes", numHashTables=5)

model = mh.fit(dfA)

print("The hashed dataset where hashed values are stored in the column 'hashes':")
model.transform(dfA).show()

print("Approximately joining dfA and dfB on distance smaller than 0.6:")
model.approxSimilarityJoin(dfA, dfB, 0.6, distCol="JaccardDistance").select(col("datasetA.id").alias("idA"),col("datasetB.id").alias("idB"),col("JaccardDistance")).show()

# May return less than 2 rows when not enough approximate near-neighbor candidates are found.
print("Approximately searching dfA for 2 nearest neighbors of the key:")
model.approxNearestNeighbors(dfA, key, 2).show()

spark.stop()
