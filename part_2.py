from pyspark.sql import SparkSession
from pyspark.sql.functions import col
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

# You can read the data from a file into DataFrames
df = spark.read.csv("iot_details/export.csv", header=True, inferSchema=True)
sorted_df = df.orderBy(col(df.columns[2]), col(df.columns[-1]))
sorted_df.show()
