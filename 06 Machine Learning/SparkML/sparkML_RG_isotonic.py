from pyspark.ml.regression import IsotonicRegression
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

dataset = spark.read.format("libsvm").load("file:////usr/lib/spark/data/mllib/sample_isotonic_regression_libsvm_data.txt")

model = IsotonicRegression().fit(dataset)
print("Boundaries in increasing order: %s\n" % str(model.boundaries))
print("Predictions associated with the boundaries: %s\n" % str(model.predictions))

model.transform(dataset).show()

spark.stop()
