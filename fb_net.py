import networkx as nx
import requests
import gzip
import shutil
from networkx.algorithms.community import greedy_modularity_communities

# Download and extract the dataset
url = "https://snap.stanford.edu/data/facebook_combined.txt.gz"
response = requests.get(url, stream=True)
with open('facebook_combined.txt.gz', 'wb') as f:
    f.write(response.content)

# Unzip the file
with gzip.open('facebook_combined.txt.gz', 'rb') as f_in:
    with open('facebook_combined.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# Load the graph
facebook_graph = nx.read_edgelist('facebook_combined.txt', create_using=nx.Graph(), nodetype=int)

# Detect communities
communities = greedy_modularity_communities(facebook_graph)

# Print community information
print(f"Number of communities detected: {len(communities)}")
for i, community in enumerate(communities):
    print(f"Community {i+1}: {len(community)} nodes")

# Degree Centrality
degree_centrality = nx.degree_centrality(facebook_graph)
top_5_central_nodes = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5]

print("Top 5 Central Nodes by Degree Centrality:")
for node, centrality in top_5_central_nodes:
    print(f"Node {node} with centrality {centrality:.2f}")

# Betweenness Centrality
betweenness_centrality = nx.betweenness_centrality(facebook_graph)
top_5_betweenness_nodes = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:5]

print("Top 5 Nodes by Betweenness Centrality:")
for node, centrality in top_5_betweenness_nodes:
    print(f"Node {node} with betweenness centrality {centrality:.2f}")

# Closeness Centrality
closeness_centrality = nx.closeness_centrality(facebook_graph)
top_5_closeness_nodes = sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True)[:5]

print("Top 5 Nodes by Closeness Centrality:")
for node, centrality in top_5_closeness_nodes:
    print(f"Node {node} with closeness centrality {centrality:.2f}")

# Eigenvector Centrality
eigenvector_centrality = nx.eigenvector_centrality(facebook_graph)
top_5_eigenvector_nodes = sorted(eigenvector_centrality.items(), key=lambda x: x[1], reverse=True)[:5]

print("Top 5 Nodes by Eigenvector Centrality:")
for node, centrality in top_5_eigenvector_nodes:
    print(f"Node {node} with eigenvector centrality {centrality:.2f}")

# Clustering Coefficient
avg_clustering_coefficient = nx.average_clustering(facebook_graph)
print(f"Average Clustering Coefficient: {avg_clustering_coefficient:.4f}")

# Path Length Statistics
if nx.is_connected(facebook_graph):
    avg_shortest_path_length = nx.average_shortest_path_length(facebook_graph)
    diameter = nx.diameter(facebook_graph)
    print(f"Average Shortest Path Length: {avg_shortest_path_length:.4f}")
    print(f"Diameter of the Network: {diameter}")
else:
    print("The graph is not connected, so path length and diameter statistics are not applicable.")

# Save the graph in GEXF format
nx.write_gexf(facebook_graph, 'facebook_combined.gexf')