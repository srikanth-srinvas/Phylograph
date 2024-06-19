import numpy as np

def calculate_distance_matrix(sequences):
    ids = list(sequences.keys())
    num_sequences = len(ids)
    distance_matrix = np.zeros((num_sequences, num_sequences))

    for i in range(num_sequences):
        for j in range(i + 1, num_sequences):
            distance = calculate_distance(sequences[ids[i]], sequences[ids[j]])
            distance_matrix[i, j] = distance
            distance_matrix[j, i] = distance

    return distance_matrix

def calculate_distance(seq1, seq2):
    differences = sum(1 for a, b in zip(seq1, seq2) if a != b)
    return differences / len(seq1)