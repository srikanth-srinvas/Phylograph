import sys
from Bio import SeqIO
from clustering import calculate_distance_matrix, upgma, get_newick_format
from visualization import plot_tree

def main(input_file, output_file):
    sequences = [str(record.seq) for record in SeqIO.parse(input_file, "fasta")]
    distance_matrix = calculate_distance_matrix(sequences)
    clusters, heights = upgma(distance_matrix)
    root = max(clusters.keys())
    newick_str = get_newick_format(clusters, heights, root)
    plot_tree(newick_str, output_file)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)