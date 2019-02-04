from pyspark.ml.classification import LinearSVC
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

training = spark.read.format("libsvm").load("file:///usr/lib/spark/data/mllib/sample_libsvm_data.txt")

lsvc      = LinearSVC(maxIter=10, regParam=0.1)
lsvcModel = lsvc.fit(training)

print("Coefficients: " + str(lsvcModel.coefficients))
print("Intercept: " + str(lsvcModel.intercept))

spark.stop()
