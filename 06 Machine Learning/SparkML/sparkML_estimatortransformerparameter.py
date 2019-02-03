from pyspark.ml.linalg import Vectors
from pyspark.ml.classification import LogisticRegression
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

training = spark.createDataFrame([
                                  (1.0, Vectors.dense([0.0, 1.1, 0.1])),
                                  (0.0, Vectors.dense([2.0, 1.0, -1.0])),
                                  (0.0, Vectors.dense([2.0, 1.3, 1.0])),
                                  (1.0, Vectors.dense([0.0, 1.2, -0.5]))
                                 ], ["label", "features"])

# Estimator
lr     = LogisticRegression(maxIter=10, regParam=0.01)
print("LogisticRegression parameters:\n" + lr.explainParams() + "\n")

# Transformer
model1 = lr.fit(training)
print("Model 1 was fit using parameters: ")
print(model1.extractParamMap())

# Parameters
paramMap             = {lr.maxIter: 20}
paramMap[lr.maxIter] = 30
paramMap.update({lr.regParam: 0.1, lr.threshold: 0.55})

paramMap2        = {lr.probabilityCol: "myProbability"}

paramMapCombined = paramMap.copy()
paramMapCombined.update(paramMap2)

# Transformer
model2 = lr.fit(training, paramMapCombined)
print("Model 2 was fit using parameters: ")
print(model2.extractParamMap())

test = spark.createDataFrame([
                              (1.0, Vectors.dense([-1.0, 1.5, 1.3])),
                              (0.0, Vectors.dense([3.0, 2.0, -0.1])),
                              (1.0, Vectors.dense([0.0, 2.2, -1.5]))
                             ], ["label", "features"])

prediction = model2.transform(test)
result = prediction.select("features", "label", "myProbability", "prediction").collect()

for row in result:
  print("features=%s, label=%s -> prob=%s, prediction=%s" % (row.features, row.label, row.myProbability, row.prediction))

spark.stop()
