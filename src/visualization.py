import matplotlib.pyplot as plt
from Bio import Phylo
from io import StringIO

def plot_tree(newick_str, output_file):
    tree = Phylo.read(StringIO(newick_str), "newick")
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(1, 1, 1)

    Phylo.draw(tree, do_show=False, axes=ax, branch_labels=lambda c: round(c.branch_length, 2) if c.branch_length else '')

    for clade in tree.find_clades():
        if clade.is_terminal():
            x = ax.get_xlim()[1]
            y = ax.transData.transform((0, clade.y))[1]
            ax.text(x, y, clade.name, fontsize=12, verticalalignment='center', color='blue')

    ax.axis("off")
    plt.savefig(output_file)
    plt.close()
