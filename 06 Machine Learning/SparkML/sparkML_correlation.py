from pyspark.ml.linalg import Vectors
from pyspark.ml.stat import Correlation
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

data = [
        (Vectors.dense([21.0 , 110 , 3.90]),),
        (Vectors.dense([22.8 , 93  , 3.85]),),
        (Vectors.dense([18.1 , 105 , 2.76]),)
       ]

df = spark.createDataFrame(data, ['features'])
r1 = Correlation.corr(df, 'features', 'pearson').head()
r2 = Correlation.corr(df, 'features', 'spearman').head()

print 'Data:'
print df.show()

print 'Pearson Correlation:'
print str(r1[0])

print 'Spearman Correlation:'
print str(r2[0])

spark.stop()
