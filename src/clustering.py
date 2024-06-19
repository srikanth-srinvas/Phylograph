import numpy as np
from collections import defaultdict

def calculate_distance_matrix(sequences):
    # Calculate the distance matrix
    num_sequences = len(sequences)
    distance_matrix = np.zeros((num_sequences, num_sequences))
    for i in range(num_sequences):
        for j in range(i + 1, num_sequences):
            distance = np.sum(np.array(sequences[i]) != np.array(sequences[j]))
            distance_matrix[i, j] = distance
            distance_matrix[j, i] = distance
    return distance_matrix

def upgma(distance_matrix):
    # Implement the UPGMA algorithm
    num_sequences = len(distance_matrix)
    clusters = {i: [i] for i in range(num_sequences)}
    heights = {i: 0 for i in range(num_sequences)}

    while len(clusters) > 1:
        # Find the closest clusters
        min_dist = np.inf
        to_merge = None
        for i in clusters:
            for j in clusters:
                if i != j and distance_matrix[i, j] < min_dist:
                    min_dist = distance_matrix[i, j]
                    to_merge = (i, j)

        if to_merge is None:
            break

        i, j = to_merge
        new_cluster = clusters[i] + clusters[j]
        new_id = max(clusters.keys()) + 1

        # Update the distance matrix
        for k in clusters:
            if k != i and k != j:
                distance_matrix = np.pad(distance_matrix, ((0, 1), (0, 1)), mode='constant', constant_values=0)
                distance_matrix[new_id, k] = np.mean([distance_matrix[x, k] for x in new_cluster for y in clusters[k]])
                distance_matrix[k, new_id] = distance_matrix[new_id, k]

        # Add the new cluster to clusters and heights
        clusters[new_id] = new_cluster
        heights[new_id] = min_dist / 2

        # Remove the old clusters
        del clusters[i]
        del clusters[j]

    return clusters, heights

def get_newick_format(clusters, heights, root):
    if len(clusters[root]) == 1:
        return f"{clusters[root][0]}:{heights[root]}"

    children = clusters[root]
    left = children[:len(children)//2]
    right = children[len(children)//2:]

    left_id = [k for k, v in clusters.items() if v == left][0]
    right_id = [k for k, v in clusters.items() if v == right][0]

    left_newick = get_newick_format(clusters, heights, left_id)
    right_newick = get_newick_format(clusters, heights, right_id)

    return f"({left_newick},{right_newick}):{heights[root]}"
