from pyspark.ml.regression import AFTSurvivalRegression
from pyspark.ml.linalg import Vectors
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

training = spark.createDataFrame([
                                  (1.218, 1.0, Vectors.dense(1.560, -0.605)),
                                  (2.949, 0.0, Vectors.dense(0.346, 2.158)),
                                  (3.627, 0.0, Vectors.dense(1.380, 0.231)),
                                  (0.273, 1.0, Vectors.dense(0.520, 1.151)),
                                  (4.199, 0.0, Vectors.dense(0.795, -0.226))
                                 ], ["label", "censor", "features"])

quantileProbabilities = [0.3, 0.6]

aft   = AFTSurvivalRegression(quantileProbabilities=quantileProbabilities,quantilesCol="quantiles")
model = aft.fit(training)

print("Coefficients: " + str(model.coefficients))
print("Intercept: " + str(model.intercept))
print("Scale: " + str(model.scale))
model.transform(training).show(truncate=False)

spark.stop()
