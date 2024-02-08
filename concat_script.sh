#!/bin/bash

# Directory containing XML files
input_directory="/proj/uwmadison744-s24-PG0/data-part3/enwiki-pages-articles"

# Output file
output_file="concatenated_output.xml"

# List of XML files to concatenate
echo $file_count
xml_files=($(ls -1 "$input_directory"/*.xml*))

# Concatenate the XML files
cat "${xml_files[@]}" > "$output_file"

echo "Concatenation complete. Output file: $output_file"
