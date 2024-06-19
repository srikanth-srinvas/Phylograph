import numpy as np

def calculate_distance_matrix(sequences):
    num_sequences = len(sequences)
    distance_matrix = np.zeros((num_sequences, num_sequences))
    for i in range(num_sequences):
        for j in range(i + 1, num_sequences):
            distance = np.sum(np.array(sequences[i]) != np.array(sequences[j]))
            distance_matrix[i, j] = distance
            distance_matrix[j, i] = distance
    return distance_matrix

def upgma(distance_matrix):
    num_sequences = len(distance_matrix)
    clusters = {i: [i] for i in range(num_sequences)}
    heights = {i: 0 for i in range(num_sequences)}
    cluster_distances = distance_matrix.copy()

    while len(clusters) > 1:
        # Find the closest clusters
        min_dist = np.inf
        to_merge = None
        for i in clusters:
            for j in clusters:
                if i != j and cluster_distances[i, j] < min_dist:
                    min_dist = cluster_distances[i, j]
                    to_merge = (i, j)

        if to_merge is None:
            break

        i, j = to_merge
        new_cluster = clusters[i] + clusters[j]
        new_id = max(clusters.keys()) + 1

        # Update the distance matrix
        cluster_distances = np.pad(cluster_distances, ((0, 1), (0, 1)), mode='constant', constant_values=np.inf)
        for k in clusters:
            if k != i and k != j:
                cluster_distances[new_id, k] = np.mean([cluster_distances[x, k] for x in new_cluster])
                cluster_distances[k, new_id] = cluster_distances[new_id, k]

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

    left_id = [k for k, v in clusters.items() if set(v) == set(left)]
    right_id = [k for k, v in clusters.items() if set(v) == set(right)]

    left_newick = get_newick_format(clusters, heights, left_id[0]) if left_id else f"{left}:{heights[root]}"
    right_newick = get_newick_format(clusters, heights, right_id[0]) if right_id else f"{right}:{heights[root]}"

    return f"({left_newick},{right_newick}):{heights[root]}"
