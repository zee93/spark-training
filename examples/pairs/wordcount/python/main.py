import os
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("test")
sc = SparkContext(conf=conf)

cwd = os.path.dirname(os.path.dirname(__file__))
words_count_rdd = (sc.
                   textFile(cwd + '/input')
                   .flatMap(lambda l: l.split(' '))
                   .filter(lambda x: x != '' and x != '.')
                   .map(lambda x: (x.lower(), 1))
                   .reduceByKey(lambda a, b: a + b)
                   )
words_count_rdd.saveAsTextFile('output')
