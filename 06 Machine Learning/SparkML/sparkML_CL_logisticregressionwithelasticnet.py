from pyspark.ml.classification import LogisticRegression
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

training = spark.read.format("libsvm").load("file:///usr/lib/spark/data/mllib/sample_libsvm_data.txt")

lr      = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)
lrModel = lr.fit(training)
print("Coefficients: " + str(lrModel.coefficients))
print("Intercept: " + str(lrModel.intercept))

mlr      = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8, family="multinomial")
mlrModel = mlr.fit(training)
print("Multinomial coefficients: " + str(mlrModel.coefficientMatrix))
print("Multinomial intercepts: " + str(mlrModel.interceptVector))

spark.stop()
