import matplotlib.pyplot as plt
from Bio import Phylo
from io import StringIO

def plot_tree(newick_str, output_file):
    handle = StringIO(newick_str)
    tree = Phylo.read(handle, "newick")
    
    fig = plt.figure(figsize=(10, 5), dpi=100)
    axes = fig.add_subplot(1, 1, 1)
    
    Phylo.draw(tree, axes=axes, do_show=False)
    plt.savefig(output_file)
    plt.close()