from pyspark import SparkContext, SparkConf
from pyspark import SQLContext
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.clustering import KMeans
from os.path import dirname


conf = SparkConf().setAppName("test")
sc = SparkContext(conf=conf)

sc = SQLContext(sc)

path = dirname(dirname(__file__))
data = sc.jsonFile(path + "/data/tweets/*/*")
data.registerTempTable("tweets")

tf = HashingTF(numFeatures=10000)


def featurize(str):
    return tf.transform(str.split())
vectors = data.map(featurize).cache()

model = KMeans.train(vectors, 5, 100)
groups = data.groupBy(lambda t: model.predict(featurize(t)))
for each in groups:
    print(each)
model.predict(featurize("test"))
