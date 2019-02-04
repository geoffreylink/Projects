import sys
if sys.version >= '3':
    long = int
from pyspark.sql import SparkSession
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql import Row

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

lines      = spark.read.text("file:///usr/lib/spark/data/mllib/als/sample_movielens_ratings.txt").rdd
parts      = lines.map(lambda row: row.value.split("::"))
ratingsRDD = parts.map(lambda p: Row(userId=int(p[0]), movieId=int(p[1]),rating=float(p[2]), timestamp=long(p[3])))
ratings    = spark.createDataFrame(ratingsRDD)

(training, test) = ratings.randomSplit([0.8, 0.2])

# Note we set cold start strategy to 'drop' to ensure we don't get NaN evaluation metrics
als   = ALS(maxIter=5, regParam=0.01, userCol="userId", itemCol="movieId", ratingCol="rating",coldStartStrategy="drop")
model = als.fit(training)

predictions = model.transform(test)
evaluator   = RegressionEvaluator(metricName="rmse", labelCol="rating",predictionCol="prediction")
rmse        = evaluator.evaluate(predictions)
print("Root-mean-square error = " + str(rmse))

userRecs  = model.recommendForAllUsers(10)
movieRecs = model.recommendForAllItems(10)

users          = ratings.select(als.getUserCol()).distinct().limit(3)
userSubsetRecs = model.recommendForUserSubset(users, 10)

movies          = ratings.select(als.getItemCol()).distinct().limit(3)
movieSubSetRecs = model.recommendForItemSubset(movies, 10)

userRecs.show()
movieRecs.show()
userSubsetRecs.show()
movieSubSetRecs.show()

spark.stop()
