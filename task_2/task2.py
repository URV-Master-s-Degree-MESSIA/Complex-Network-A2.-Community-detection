'''
Characterization of the community structure of real networks

In this part of the activity, you should use algorithms relying on modularity maximization to analyze the community
structure of a real network capturing face-to-face interactions in a primary school in France. 
In this network, nodes represent either students or teachers and weights are proportional to the time they were 
together during the two days in which interactions were measured. More information on the network can be found here: 

http://www.sociopatterns.org/publications/high-resolution-measurements-of-face-to-face-contact-patterns-in-a-primary-school/


You should analyze both the unweighted (‘primaryschool_u.net’) and the weighted (‘primaryschool_w.net’) versions of this network. 
In addition, node metadata is available (metadata_primary_school.txt), indicating the school group each individual belongs to.

The report must include:

    A comparison between the community structure found in both the unweighted and the weighted networks. 
    Use a color-coded representation, similar to the one explained in the previous activity. 
    The position of the nodes should be set by applying the chosen positioning algorithm to the weighted network. Warning: 
        If you choose the Kamada-Kawai layout algorithm to visualize the network, 
        the weights introduced in the algorithm should be the inverse (1/wij) of 
        the actual weights (wij) of the network. Nonetheless, you should keep using 
        the actual weights for community detection. 
    The composition of the detected communities in terms of the school groups to which their individuals belong. 
    You should provide a visual representation (e.g. a stacked bar plot, a pie chart) to show how many individuals 
    of each school group are in each community.
    A brief discussion on the differences among the communities detected in the weighted and unweighted network. 
    Why weights are relevant?
'''
import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from task_1.task_1_utils import load_network
from task_2.algos import detect_louvain_communities
from task_2.visualization import draw_network
from task_2.utils import get_node_community_map, plot_community_composition;


# Base PATH:
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../data/A3_primary_school_network")
nets = ["primaryschool_u.net", "primaryschool_w.net"]


net1 = os.path.join(DATA_DIR, nets[0])
net2 = os.path.join(DATA_DIR, nets[1])
metadata = os.path.join(DATA_DIR, "metadata_primary_school.txt")

# Metadata:
metadata = pd.read_csv(metadata, sep='\s+', header=None)
metadata.columns = ['Id', 'Group']
metadata['Id'] = metadata['Id'].astype(str) 

# Load nets.
G_u = load_network(net1)
G_u = nx.Graph(G_u)

G_w = load_network(net2)
G_w = nx.Graph(G_w)  # Convertir a undirected simple graph
for u, v, d in G_w.edges(data=True):
    d['weight'] = float(d['weight'])


# Detect communities with Louvain algorithm:
communities_w = detect_louvain_communities(G_w, weighted=True)
communities_u = detect_louvain_communities(G_u, weighted=False)

# Invertir pesos para Kamada-Kawai layout
G_layout = G_w.copy()
for u, v, d in G_layout.edges(data=True):
    d['weight'] = 1.0 / d['weight']

pos = nx.kamada_kawai_layout(G_layout, weight='weight')


draw_network(G_w, communities_w, pos, "Communities (Weighted Network)")
draw_network(G_u, communities_u, pos, "Communities (Unweighted Network)")

metadata['Community_W'] = metadata['Id'].map(get_node_community_map(communities_w))
metadata['Community_U'] = metadata['Id'].map(get_node_community_map(communities_u))

plot_community_composition(
    metadata,
    community_col='Community_W',
    title="Composition of Communities (Weighted Network)",
    filename="composition_weighted.png"  # O usa None para mostrar
)

plot_community_composition(
    metadata,
    community_col='Community_U',
    title="Composition of Communities (Unweighted Network)",
    filename="composition_unweighted.png"
)