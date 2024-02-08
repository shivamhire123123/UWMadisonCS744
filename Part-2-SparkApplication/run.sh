# Run a Python application on a Spark standalone cluster
wget http://pages.cs.wisc.edu/~shivaram/cs744-fa18/assets/export.csv

hdfs dfs -rm -r -f hdfs:///result

hdfs dfs -rm hdfs://10.10.1.1:9000/export.csv

hdfs dfs -copyFromLocal export.csv hdfs:///export.csv

/mnt/data/spark-3.3.4-bin-hadoop3/bin/spark-submit \
  --master spark://node0.cs744s24-g22.uwmadison744-s24-pg0.wisc.cloudlab.us:7077 \
  /mnt/data/Part-2-SparkApplication/part_2.py \
  --input hdfs://10.10.1.1:9000/export.csv \
  --output hdfs://10.10.1.1:9000/result