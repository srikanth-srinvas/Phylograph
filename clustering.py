import numpy as np

class Node:
    def __init__(self, left=None, right=None, distance=0.0, id=None):
        self.left = left
        self.right = right
        self.distance = distance
        self.id = id

def upgma(distance_matrix):
    num_sequences = len(distance_matrix)
    clusters = {i: [i] for i in range(num_sequences)}
    nodes = {i: Node(id=i) for i in range(num_sequences)}

    while len(clusters) > 1:
        min_distance = np.inf
        for i in clusters:
            for j in clusters:
                if i < j:
                    dist = np.mean([distance_matrix[x][y] for x in clusters[i] for y in clusters[j]])
                    if dist < min_distance:
                        min_distance = dist
                        to_merge = (i, j)

        i, j = to_merge
        new_id = max(nodes.keys()) + 1
        new_node = Node(left=nodes[i], right=nodes[j], distance=min_distance / 2.0, id=new_id)
        nodes[new_id] = new_node

        new_cluster = clusters[i] + clusters[j]
        del clusters[i]
        del clusters[j]
        clusters[new_id] = new_cluster

        for k in clusters:
            distance_matrix[new_id][k] = np.mean([distance_matrix[x][y] for x in new_cluster for y in clusters[k]])
            distance_matrix[k][new_id] = distance_matrix[new_id][k]

    return nodes[new_id]
