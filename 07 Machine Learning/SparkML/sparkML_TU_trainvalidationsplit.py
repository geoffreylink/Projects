from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.regression import LinearRegression
from pyspark.ml.tuning import ParamGridBuilder, TrainValidationSplit
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

data        = spark.read.format("libsvm").load("file:///usr/lib/spark/data/mllib/sample_linear_regression_data.txt")
train, test = data.randomSplit([0.9, 0.1], seed=12345)

lr = LinearRegression(maxIter=10)

paramGrid = ParamGridBuilder().addGrid(lr.regParam, [0.1, 0.01]).addGrid(lr.fitIntercept, [False, True]).addGrid(lr.elasticNetParam, [0.0, 0.5, 1.0]).build()

tvs = TrainValidationSplit(estimator          = lr,
                           estimatorParamMaps = paramGrid,
                           evaluator          = RegressionEvaluator(),
                           trainRatio         = 0.8)

model = tvs.fit(train)

model.transform(test).select("features", "label", "prediction").show()

spark.stop()
