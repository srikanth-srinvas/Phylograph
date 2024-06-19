import sys
from distance_matrix import calculate_distance_matrix
from clustering import upgma, get_newick_format
from visualization import plot_tree
from Bio import SeqIO

def main(input_file, output_file):
    sequences, labels = read_fasta(input_file)
    distance_matrix = calculate_distance_matrix(sequences)
    clusters, heights, root = upgma(distance_matrix)
    newick_str = get_newick_format(clusters, heights, root, labels)
    plot_tree(newick_str, output_file)

def read_fasta(file_path):
    sequences = []
    labels = []
    with open(file_path, 'r') as file:
        for record in SeqIO.parse(file, "fasta"):
            sequences.append(str(record.seq))
            labels.append(record.id)
    return sequences, labels

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_fasta_file> <output_image_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
