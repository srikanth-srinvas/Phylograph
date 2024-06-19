import numpy as np

def calculate_distance_matrix(sequences):
    num_seqs = len(sequences)
    dist_matrix = np.zeros((num_seqs, num_seqs))
    for i in range(num_seqs):
        for j in range(i + 1, num_seqs):
            dist = np.sum([1 for a, b in zip(sequences[i], sequences[j]) if a != b])
            dist_matrix[i][j] = dist
            dist_matrix[j][i] = dist
    return dist_matrix

def upgma(distance_matrix):
    clusters = {i: [i] for i in range(len(distance_matrix))}
    heights = {i: 0 for i in range(len(distance_matrix))}
    while len(clusters) > 1:
        min_dist = float("inf")
        to_merge = None
        for i in clusters:
            for j in clusters:
                if i < j and distance_matrix[i, j] < min_dist:
                    min_dist = distance_matrix[i, j]
                    to_merge = (i, j)
        
        if not to_merge:
            break

        i, j = to_merge
        new_cluster = clusters[i] + clusters[j]
        new_id = min(clusters.keys()) + len(clusters)
        clusters[new_id] = new_cluster
        heights[new_id] = min_dist / 2
        
        for k in clusters:
            if k != i and k != j and k != new_id:
                distance_matrix[new_id][k] = np.mean([distance_matrix[x][y] for x in new_cluster for y in clusters[k]])
                distance_matrix[k][new_id] = distance_matrix[new_id][k]
        
        del clusters[i]
        del clusters[j]
    
    root = max(clusters.keys())
    return clusters, heights, root

def get_newick_format(clusters, heights, root, labels):
    def recurse(node):
        if len(clusters[node]) == 1:
            return labels[clusters[node][0]]
        left, right = clusters[node][:len(clusters[node]) // 2], clusters[node][len(clusters[node]) // 2:]
        left_id = [k for k, v in clusters.items() if v == left][0]
        right_id = [k for k, v in clusters.items() if v == right][0]
        left_str = recurse(left_id)
        right_str = recurse(right_id)
        return f"({left_str}:{heights[node] - heights[left_id]},{right_str}:{heights[node] - heights[right_id]})"
    return recurse(root) + ";"
