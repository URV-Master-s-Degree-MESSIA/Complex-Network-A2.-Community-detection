import community as community_louvain
from collections import defaultdict

def detect_louvain_communities(G, weighted=True):
    '''
        Function to detect communities in a graph using Louvain's algorithm.
        Depending on the 'weighted' flag, edge weights will be used or not.
        :param G: NetworkX graph
        :param weighted: Boolean indicating whether to consider edge weights.
        :return: List of communities, where each community is a list of nodes.
    '''
    if weighted:
        partition = community_louvain.best_partition(G, weight='weight')
    else:
        partition = community_louvain.best_partition(G)

    communities = defaultdict(list)
    for node, comm in partition.items():
        communities[comm].append(node)
    return list(communities.values())
    

