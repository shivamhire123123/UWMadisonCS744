from pyspark import SparkConf, SparkContext

def parse_line(line):
    """Parse a line of the input data."""
    parts = line.split('\t')
    print("***********")
    print(parts)
    print("*"*8)
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
    input_path = "hdfs://10.10.1.1:9000/concatenated_output.xml"
    lines = sc.textFile(input_path)
    print("Type of lines : = ",type(lines))

    # Parse the input data
    links = lines.map(parse_line).distinct().groupByKey()
    num_pages = links.count()
    print("num pages = ",num_pages)

    # Initialize ranks
    ranks = links.mapValues(lambda v: 1.0)

    # Perform 10 iterations of PageRank
    for iteration in range(3):
        ranks = pagerank_iterate(links, ranks)

    # Output the final PageRank results
    #results = ranks.collect()

    ranks.coalesce(1).saveAsTextFile("hdfs://10.10.1.1:9000/wiki_pagerank_results.txt")
    sc.stop()
