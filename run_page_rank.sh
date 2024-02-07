# Run a Python application on a Spark standalone cluster
time /mnt/data/spark-3.3.4-bin-hadoop3/bin/spark-submit \
  --master spark://node0.cs744s24-g22.uwmadison744-s24-pg0.wisc.cloudlab.us:7077 \
  /mnt/data/page_rank/pageRank.py \
  --input hdfs://10.10.1.1:9000/web-BerkStan.txt \
  --output hdfs://10.10.1.1:9000/result1 \
  --partition 16
