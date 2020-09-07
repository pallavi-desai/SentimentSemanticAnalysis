import sys

from pyspark import SparkContext, SparkConf

if __name__ == "__main__":

  conf = SparkConf().setAppName("Spark Count")
  sc = SparkContext(conf=conf)

  wordList = ['education','canada','university','dalhousie','expensive','good school','good schools', 'bad school','bad schools', 'poor school','poor schools','faculty','computer science','graduate']

  tokenized = sc.textFile(sys.argv[1]).flatMap(lambda line: line.split(" "))

  wordCounts = tokenized.map(lambda word: (word, 1)).reduceByKey(lambda v1,v2:v1 +v2)

  filtered = wordCounts.filter(lambda pair:pair[0].lower() in wordList)

  list1 = filtered.collect()
  print("------------------------------------------------------------------------------------------------------------------")
  print repr(list1)[1:-1]
  print("------------------------------------------------------------------------------------------------------------------")
