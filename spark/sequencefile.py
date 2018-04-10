from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('sequenceFile').setMaster("local")
sc = SparkContext(conf = conf)

rdd = sc.parallelize(range(1,4)).map(lambda x: (x, "a"*x))
rdd.saveAsSequenceFile('result')
for i in sorted(sc.sequenceFile('result').collect()):
    print(i)
