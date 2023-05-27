from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test")

sc = SparkContext(conf=conf)

print(sc.version)

sc.stop()
