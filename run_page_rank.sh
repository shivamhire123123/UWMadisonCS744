# Run a Python application on a Spark standalone cluster
hdfs dfs -rm -r -f hdfs:///wiki_pagerank_results.txt
time /mnt/data/spark-3.3.4-bin-hadoop3/bin/spark-submit \
  --master spark://node0.cs744s24-g22.uwmadison744-s24-pg0.wisc.cloudlab.us:7077 \
  /mnt/data/page_rank/xmlPageRank.py \
  --input hdfs://10.10.1.1:9000/web-BerkStan.txt \
  --output hdfs://10.10.1.1:9000/result1 \
  --partition 4
