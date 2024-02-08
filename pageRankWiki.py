from pyspark import SparkConf, SparkContext
import os

def parse_line(line):
    """Parse a line of the input data."""
    parts = line.split()
    return parts[0], parts[1]

def compute_contributions(urls, rank):
    """Calculate URL contributions to the rank of other URLs."""
    num_urls = len(urls)
    for url in urls:
        yield (url, rank / num_urls)

def pagerank_iterate(links, ranks):
    """Perform one iteration of the PageRank algorithm."""
    # Calculate URL contributions to the rank of other URLs
    contributions = links.join(ranks).partitionBy(400).flatMap(
        lambda x: compute_contributions(x[1][0], x[1][1])
    )   

    # Sum up contributions by key (URL)
    new_ranks = contributions.reduceByKey(lambda x, y: x + y)

    # Apply the damping factor and add random jump factor
    damping_factor = 0.85
    jump_factor = 0.15 #/ num_pages
    new_ranks = new_ranks.mapValues(lambda rank: damping_factor * rank + jump_factor)

    return new_ranks

if __name__ == "__main__":

    # Set up Spark
    conf = SparkConf().setAppName("PageRank")
    sc = SparkContext(conf=conf)
    # Load input data from HDFS
    input_path = "hdfs://10.10.1.1:9000/wiki_articles/enwiki-pages-articles/"

    path = "/proj/uwmadison744-s24-PG0/data-part3/enwiki-pages-articles/"
    files = [input_path + filename for filename in os.listdir(path) if ".xml" in filename]

    appended_rdd = sc.textFile(files[0])

    for file_name in files[1:]:
        lines = sc.textFile(file_name)
        appended_rdd = appended_rdd.union(lines)

    lines = appended_rdd
    #lines = sc.textFile(input_path)
    #lines_prdd = sc.wholeTextFiles(input_path).values()
    #lines = lines_prdd.persist()
    print("Type of lines : = ",type(lines))
    # Parse the input data
    links = lines.map(parse_line).distinct().groupByKey()
    #num_pages = links.count()

    print("Type of links = ",type(links))

    # Initialize ranks
    ranks = links.mapValues(lambda v: 1.0)

    # Perform 10 iterations of PageRank
    for iteration in range(3):
        ranks = pagerank_iterate(links, ranks)

    print("Type of ranks = ",type(ranks))
    # Output the final PageRank results
    results = ranks.collect()
    #result_ll = ranks.map( lambda elem: list(elem))

    idx = 0
    print("Ranks computed")
    #for result in ranks:
     #   idx = idx + 1
      #  if idx == 10:
      #      break
      #  print(f"{result[0]}: {result[1]}")

    # Stop Spark
    sc.stop()
