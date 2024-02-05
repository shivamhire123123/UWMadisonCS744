# Run a Python application on a Spark standalone cluster
/mnt/data/spark-3.3.4-bin-hadoop3/bin/spark-submit \
  --master spark://10.10.1.1:7077 \
  /mnt/data/iot_details/part_2.py \
  --input /mnt/data/iot_details/export.csv \
  --output /mnt/data/iot_details/result
