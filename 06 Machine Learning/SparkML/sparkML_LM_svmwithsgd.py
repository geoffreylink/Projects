from pyspark import SparkContext
from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint

sc = SparkContext(appName="PythonSVMWithSGDExample")
sc.setLogLevel('ERROR')

def parsePoint(line):
  values = [float(x) for x in line.split(' ')]
  return LabeledPoint(values[0], values[1:])

data       = sc.textFile("file:///usr/lib/spark/data/mllib/sample_svm_data.txt")
parsedData = data.map(parsePoint)

model = SVMWithSGD.train(parsedData, iterations=100)

labelsAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
trainErr = labelsAndPreds.filter(lambda lp: lp[0] != lp[1]).count() / float(parsedData.count())
print("Training Error = " + str(trainErr))

model.save(sc, "/home/hadoop/pythonSVMWithSGDModel-01")
sameModel = SVMModel.load(sc, "/home/hadoop/pythonSVMWithSGDModel-01")
