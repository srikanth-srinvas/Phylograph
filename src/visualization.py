import matplotlib.pyplot as plt

def plot_tree(node, output_file, depth=0, pos=0, positions=None, labels=None):
    if positions is None:
        positions = {}
    if labels is None:
        labels = {}

    positions[node.id] = (depth, pos)
    if node.left is not None:
        pos = plot_tree(node.left, output_file, depth + 1, pos, positions, labels)
    if node.right is not None:
        pos = plot_tree(node.right, output_file, depth + 1, pos + 1, positions, labels)

    if node.left is None and node.right is None:
        labels[node.id] = node.id

    if depth == 0:
        draw_tree(positions, labels, output_file)

    return pos

def draw_tree(positions, labels, output_file):
    fig, ax = plt.subplots()
    for node_id, (x, y) in positions.items():
        if node_id in labels:
            ax.text(y, -x, labels[node_id], verticalalignment='center', horizontalalignment='right', fontsize=8)
        if node_id != 0:
            parent = next(parent_id for parent_id, children in positions.items() if node_id in children)
            parent_x, parent_y = positions[parent]
            ax.plot([y, parent_y], [-x, -parent_x], 'k-')
    ax.set_axis_off()
    plt.savefig(output_file)