import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

from task_2.utils import get_node_community_map, plot_community_composition;

def set_color_nodes(communities, G, cmap=plt.cm.tab20):
    '''
        Function that generates a set of colors depending on the number of subsets of communities.
        If the node belongs to any community, it is assigned a color from the palette, otherwise it is assigned gray.
    '''
    colors = cmap(np.linspace(0, 1, len(communities)))

    community_node = get_node_community_map(communities)

    color_nodes = []
    for node in G.nodes():
        color_index = community_node.get(node, -1)
        color_nodes.append('gray' if color_index == -1 else colors[color_index])
    return color_nodes


def draw_network(G, communities, pos, title):
    '''
        Function to display the graph of communities with the color of each one.
        Edge color = gray + . transparent.
    '''
    colors = set_color_nodes(communities, G)
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, node_color=colors, with_labels=False, node_size=50, edge_color='gray', alpha=0.3)
    plt.title(title)
    plt.axis('off')
    # plt.show()
    plt.savefig(f"{title.replace(' ', '_')}.png")

