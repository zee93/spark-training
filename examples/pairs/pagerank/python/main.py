from pyspark import SparkContext, SparkConf
import os


conf = SparkConf().setAppName("test")
sc = SparkContext(conf=conf)
_dir = os.path.dirname(os.path.dirname(__file__))
input_file = sc.textFile(_dir + '/input')

lines = (
    input_file
    .map(lambda l: l.split(": "))
    .map(lambda l: (l[0], l[1].split(", ")))
)  # (a, (b,c,d))

page_rank = (
    lines
    .map(lambda l: (l[0], (1.0, len(l[1]))))  # (Page, (Rank, NumOfOutgoingCons))->(Page, Contribution)
)
for i in range(3):
    print("we are in iteration number: " + str(i))
    page_contribution = page_rank.map(lambda p: (p[0], (p[1][0]/p[1][1])))  # -> (page, contribution)
    contribution_rdd = (
        page_contribution
        .leftOuterJoin(lines)  # (page, (Contribution, a,b,c,d,...))
        .flatMap(lambda con: ((con[0], (to, con[1][0])) for to in con[1][1]))
        .map(lambda con: (con[1][0], con[1][1]))
    )  # (to, contribution)
    page_rank = (
        page_rank
        .join(contribution_rdd)  # (Page, ((Rank, NumOfOutgoingConnections), contrib, contrib,..))
        .map(lambda x: ((x[0], x[1][0]), x[1][1]))
        .reduceByKey(lambda a, b: a+b)
        .map(lambda pr: (pr[0][0], (pr[1]*0.85 + 0.15, pr[0][1][1])))
    )
print("################################################")
print(page_rank.collect())
page_rank.saveAsTextFile("output")
