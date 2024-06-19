import sys
from sequence_reader import read_fasta
from distance_matrix import calculate_distance_matrix
from clustering import upgma
from visualization import plot_tree

def main(input_file, output_file):
    sequences = read_fasta(input_file)
    distance_matrix = calculate_distance_matrix(sequences)
    tree = upgma(distance_matrix)
    plot_tree(tree, output_file)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_fasta_file> <output_image_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)