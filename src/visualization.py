import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from Bio import Phylo
from io import StringIO

def plot_tree(newick_str, output_file):
    handle = StringIO(newick_str)
    tree = Phylo.read(handle, "newick")

    fig = plt.figure(figsize=(10, 5), dpi=100)
    axes = fig.add_subplot(1, 1, 1)

    # Customize plot style
    plt.rcParams['lines.linewidth'] = 2  # Increase branch line width
    plt.rcParams['axes.linewidth'] = 1.5  # Increase axis line width
    plt.rcParams['xtick.major.width'] = 1.5  # Increase tick mark width
    plt.rcParams['ytick.major.width'] = 1.5  # Increase tick mark width
    plt.rcParams['font.size'] = 12  # Set font size

    # Customize colors
    cmap = plt.get_cmap('viridis')  # Choose a colormap
    node_colors = [cmap(i / len(tree.get_terminals())) for i in range(len(tree.get_terminals()))]  # Assign colors to nodes
    branch_colors = [mcolors.to_rgba(c, alpha=0.8) for c in node_colors]  # Convert colors to RGBA

    # Plot tree with customized colors
    Phylo.draw(tree, axes=axes, do_show=False, label_colors={'labels': node_colors})
    for branch, color in zip(tree.get_terminals(), branch_colors):
        branch.branch_color = color  # Assign branch colors
    plt.savefig(output_file)
    plt.close()

