import matplotlib.pyplot as plt

def get_node_community_map(communities):
    '''
        Function that receives a list of subsets (communities) and returns a dictionary, 
        i.e. adds an index to each community.

        [
            ['1', '2', '3', '4', '5', '6' ],
            ['7', '8', '9', '10', '11', '12' ],
            ['13', '19', '22', '23', '38', '52'], 
            ['26', '27', '28', '29', '31', '32' ],
        ]
        We get:
        {
            '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0,
            '7': 1, '8': 1, '9': 1, '10': 1, '11': 1, '12': 1,
            '13': 2, '19': 2, '22': 2, '23': 2, '38': 2, '52': 2, 
            '26': 3, '27': 3, '28': 3, '29': 3, '31': 3, '32': 3,
        }
    '''
    node_community = {}
    for i, community in enumerate(communities):
        for node in community:
            node_community[node] = i
    return node_community

def plot_community_composition(metadata, community_col, title, filename=None):
    """
        Plots a stacked barplot showing the composition of communities in terms of school groups.
        Params:
            - metadata: DataFrame with columns ['Group', community_col]
            - community_col: str, name of the column with the community ID (e.g. 'Community_W')
            - title: str, chart title
            - filename: str (optional), if specified it is saved as an image instead of showing
    """
    grouped = metadata.groupby([community_col, 'Group']).size().unstack(fill_value=0)

    ax = grouped.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='tab20')
    plt.title(title)
    plt.xlabel("Community")
    plt.ylabel("Number of Individuals")
    plt.legend(title="School Group", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    if filename:
        plt.savefig(filename)
        plt.close()
    else:
        plt.show()
