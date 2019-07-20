from pyspark.ml.classification import MultilayerPerceptronClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

data = spark.read.format("libsvm").load("file:///usr/lib/spark/data/mllib/sample_multiclass_classification_data.txt")

splits = data.randomSplit([0.6, 0.4], 1234)
train  = splits[0]
test   = splits[1]

layers  = [4, 5, 4, 3]
trainer = MultilayerPerceptronClassifier(maxIter=100, layers=layers, blockSize=128, seed=1234)
model   = trainer.fit(train)
result  = model.transform(test)

predictionAndLabels = result.select("prediction", "label")
evaluator           = MulticlassClassificationEvaluator(metricName="accuracy")
print("Test set accuracy = " + str(evaluator.evaluate(predictionAndLabels)))

spark.stop()
