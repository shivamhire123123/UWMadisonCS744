#!/bin/bash

# Directory containing XML files
input_directory="/proj/uwmadison744-s24-PG0/data-part3/enwiki-pages-articles"

# Output file
output_file="concatenated_input.xml"

# List of XML files to concatenate
xml_files=($(ls -1 "$input_directory"/*.xml*))

# Concatenate the XML files
cat "${xml_files[@]}" > "$output_file"

echo "Concatenation complete. Input file: $output_file"
hdfs dfs -rm hdfs://10.10.1.1:9000/concatenated_input.xml

hdfs dfs -copyFromLocal concatenated_input.xml hdfs://
echo "Copied Wiki Dataset to HDFS"

hdfs dfs -rm -r -f hdfs:///wiki_pagerank_results.txt
echo "Deleted Previous Wiki Page Rank Results (if existing)"

time /mnt/data/spark-3.3.4-bin-hadoop3/bin/spark-submit \
  --master spark://node0.cs744s24-g22.uwmadison744-s24-pg0.wisc.cloudlab.us:7077 \
  /mnt/data/WikiDataset/task1/pageRank.py \
  --input hdfs://10.10.1.1:9000/concatenated_input.xml \
  --output hdfs://10.10.1.1:9000/wiki_pagerank_results.txt \
  --partitions 4

echo "Completed Page Rank for the Wiki Dataset"
