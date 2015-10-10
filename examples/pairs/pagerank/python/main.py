from pyspark import SparkContext, SparkConf
import os


conf = SparkConf().setAppName("test")
sc = SparkContext(conf=conf)
_dir = os.path.dirname(os.path.dirname(__file__))
input_file = sc.textFile(_dir + '/input')

node_contrib = (
    input_file
    .map(lambda x: x.split(': '))
    .map(lambda t: (t[0], t[1].split(', ')))  # (a, (b, c))
    .flatMap(
        lambda node: (
            (node[0], (to, 1/len(node[1]))) for to in node[1]
            )
        )
    )  # (node, (to, contribution))
node_contrib = node_contrib.map(lambda op: (op[1][0], (op[0], op[1][1])))  # (to, (from, contrib))

node_rank = (
    input_file
    .map(lambda x: (x.split(": ")[0], 1))
)  # (node, rank)
# ###############################
for i in range(100):
    node_rank.leftOutterJoin(node_contrib)
