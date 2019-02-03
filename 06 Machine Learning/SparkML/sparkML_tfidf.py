from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

sentenceData = spark.createDataFrame([
                                      (0.0, "a b b a a a b"),
                                      (0.0, "a b a b b a a"),
                                      (1.0, "b a b bb aa b")
                                     ], ["label", "sentence"])

# TF
tokenizer      = Tokenizer(inputCol="sentence", outputCol="words")
wordsData      = tokenizer.transform(sentenceData)
hashingTF      = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=20)
featurizedData = hashingTF.transform(wordsData)
# alternatively, CountVectorizer can also be used to get term frequency vectors

# IDF
idf            = IDF(inputCol="rawFeatures", outputCol="features")
idfModel       = idf.fit(featurizedData)
rescaledData   = idfModel.transform(featurizedData)

rescaledData.show(20, False)

spark.stop()
