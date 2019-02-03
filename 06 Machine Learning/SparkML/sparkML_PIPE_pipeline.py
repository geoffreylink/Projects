from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import HashingTF, Tokenizer
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

training = spark.createDataFrame([
                                  (0, "a b c d e spark", 1.0),
                                  (1, "b d", 0.0),
                                  (2, "spark f g h", 1.0),
                                  (3, "hadoop mapreduce", 0.0)
                                 ], ["id", "text", "label"])

# Pipeline: (1)tokenizer, (2)hashingTF, (3)lr
tokenizer = Tokenizer(inputCol="text", outputCol="words")
hashingTF = HashingTF(inputCol=tokenizer.getOutputCol(), outputCol="features")
lr = LogisticRegression(maxIter=10, regParam=0.001)
pipeline = Pipeline(stages=[tokenizer, hashingTF, lr])

model = pipeline.fit(training)

test = spark.createDataFrame([
                              (4, "spark i j k"),
                              (5, "l m n"),
                              (6, "spark hadoop spark"),
                              (7, "apache hadoop")
                             ], ["id", "text"])

prediction = model.transform(test)
selected = prediction.select("id", "text", "probability", "prediction")
for row in selected.collect():
  rid, text, prob, prediction = row
  print("(%d, %s) --> prob=%s, prediction=%f" % (rid, text, str(prob), prediction))

spark.stop()
