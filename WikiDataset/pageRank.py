from pyspark import SparkConf, SparkContext
import argparse

def parse_line(line):
    """Parse a line of the input data."""
    parts = line.split('\t')
    return parts[0], parts[1]

def compute_contributions(urls, rank):
    """Calculate URL contributions to the rank of other URLs."""
    num_urls = len(urls)
    for url in urls:
        yield (url, rank / num_urls)

def pagerank_iterate(links, ranks, partitions):
    """Perform one iteration of the PageRank algorithm."""
    # Calculate URL contributions to the rank of other URLs
    contributions = links.join(ranks).partitionBy(partitions).flatMap(
        lambda x: compute_contributions(x[1][0], x[1][1])
    )   

    # Sum up contributions by key (URL)
    new_ranks = contributions.reduceByKey(lambda x, y: x + y)

    # Apply the damping factor and add random jump factor
    damping_factor = 0.85
    jump_factor = 0.15
    new_ranks = new_ranks.mapValues(lambda rank: damping_factor * rank + jump_factor)

    return new_ranks

if __name__ == "__main__":

    # Set up Spark
    conf = SparkConf().setAppName("PageRank")
    sc = SparkContext(conf=conf)

    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str)
    parser.add_argument('--output', type=str)
    parser.add_argument('--partitions', type=int)
    args = parser.parse_args()

    # Load input data from HDFS
    lines = sc.textFile(args.input)

    # Parse the input data
    links = lines.map(parse_line).distinct().groupByKey()
    links.persist()

    # Initialize ranks
    ranks = links.mapValues(lambda v: 1.0)

    # Perform 10 iterations of PageRank
    for iteration in range(1):
        ranks = pagerank_iterate(links, ranks, args.partitions)

    # Output the final PageRank results
    ranks.coalesce(1).saveAsTextFile(args.output)

    # Stop Spark
    sc.stop()
