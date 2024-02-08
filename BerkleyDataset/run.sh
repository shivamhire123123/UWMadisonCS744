#!/bin/bash

wget https://snap.stanford.edu/data/web-BerkStan.txt.gz
gzip web-BerkStan.txt.gz -d

hdfs dfs -rm hdfs://10.10.1.1:9000/web-BerkStan.txt

hdfs dfs -copyFromLocal web-BerkStan.txt hdfs://
echo "Copied Berkley Dataset to HDFS"

hdfs dfs -rm -r -f hdfs:///berkley_pagerank_results.txt
echo "Deleted Previous Berkley Dataset Page Rank Results (if existing)"

time /mnt/data/spark-3.3.4-bin-hadoop3/bin/spark-submit \
  --master spark://node0.cs744s24-g22.uwmadison744-s24-pg0.wisc.cloudlab.us:7077 \
  /mnt/data/page_rank/BerkleyDataset/pageRank.py \
  --input hdfs://10.10.1.1:9000/web-BerkStan.txt \
  --output hdfs://10.10.1.1:9000/berkley_pagerank_results.txt \
  --partitions 4

echo "Completed Page Rank for the Berkley Dataset"
