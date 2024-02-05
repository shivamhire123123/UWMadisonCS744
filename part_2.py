
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import argparse
# The entry point into all functionality in Spark is the SparkSession class.
spark = (SparkSession
	.builder
	.appName("CS744")
	.config("spark.driver.memory", "30g")
        .config("spark.executor.memory", "30g")
        .config("spark.executor.cores", "5")
        .config("spark.task.cpus", "1")
        .master("local[*]")
	.getOrCreate())

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str)
parser.add_argument('--output', type=str)
args = parser.parse_args()

# You can read the data from a file into DataFrames
#df = spark.read.csv("/mnt/data/iot_details/export.csv", header=True, inferSchema=True)
df = spark.read.csv(args.input, header=True, inferSchema=True)
sorted_df = df.orderBy(col(df.columns[2]), col(df.columns[-1]))
sorted_df.show()
#sorted_df.write.format("csv").save("result")
sorted_df.write.format("csv").save(args.output)
