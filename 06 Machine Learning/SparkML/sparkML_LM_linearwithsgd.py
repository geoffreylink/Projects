from pyspark import SparkContext
from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD, LinearRegressionModel

sc = SparkContext()
sc.setLogLevel('ERROR')

def parsePoint(line):
  values = [float(x) for x in line.replace(',', ' ').split(' ')]
  return LabeledPoint(values[0], values[1:])

data       = sc.textFile("file:///usr/lib/spark/data/mllib/ridge-data/lpsa.data")
parsedData = data.map(parsePoint)

model = LinearRegressionWithSGD.train(parsedData, iterations=100, step=0.00000001)

valuesAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
MSE            = valuesAndPreds.map(lambda vp: (vp[0] - vp[1])**2).reduce(lambda x, y: x + y) / valuesAndPreds.count()

print("Mean Squared Error = " + str(MSE))
