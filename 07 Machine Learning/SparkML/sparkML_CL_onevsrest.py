from pyspark.ml.classification import LogisticRegression, OneVsRest
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

inputData = spark.read.format("libsvm").load("file:///usr/lib/spark/data/mllib/sample_multiclass_classification_data.txt")

(train, test) = inputData.randomSplit([0.8, 0.2])

lr       = LogisticRegression(maxIter=10, tol=1E-6, fitIntercept=True)
ovr      = OneVsRest(classifier=lr)
ovrModel = ovr.fit(train)

predictions = ovrModel.transform(test)
evaluator   = MulticlassClassificationEvaluator(metricName="accuracy")
accuracy    = evaluator.evaluate(predictions)
print("Test Error = %g" % (1.0 - accuracy))

spark.stop()
