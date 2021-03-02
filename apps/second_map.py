import streamlit as st
import os
import sys
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
def app():
 # Define the number of nodes
 nodes = np.array(["v1", "v2", "v3", "v4", "v5","v6","v7","v8","v9","v10","v11","v12","v13","v14"])
 # Define the distance between nodes
 row = np.array(["v1", "v14", "v12", "v12", "v12","v13","v3","v14","v2","v2","v2","v11","v10","v3","v3","v4","v7"])
 col = np.array(["v14", "v13", "v13", "v4", "v5","v8","v9","v2","v8","v3","v4","v1","v1","v6","v7","v9","v5"])
 value = np.array([12, 25, 36, 8, 7, 10, 39, 14, 43, 15, 24, 21,17,39,17,21.15,8])
 # Generate undirected graph
 G = nx.Graph()
 # Add a node to the graph
 for i in range(0, np.size(nodes)):
    G.add_node(nodes[i])
 # Add weighted edges
 for i in range(0, np.size(row)):
    G.add_weighted_edges_from([(row[i], col[i], value[i])])
 # Set network layout
 pos = nx.random_layout(G)
 # Draw a network image
 nx.draw(G, pos, with_labels=True, node_color='white', edge_color='b', node_size=800, alpha=0.5)
 plt.ion() # Turn on interactive mode
 plt.title("slfe_Net")
 plt.ioff()
 plt.savefig("Graph.png", format="PNG")
 plt.show()
 edge_labels = nx.get_edge_attributes(G, 'weight')
 nx.draw_networkx_edge_labels(G, pos, edge_labels)
 #nx.draw_networkx_edge_labels(G, pos, edge_labels)
 image = Image.open('Graph.png')
 st.image(image)
 plt.pause(1)  # Interval seconds: 3s
 plt.close()
 # dijkstra method to find the shortest path
 start = st.text_input("Please enter the start nodes separated by spaces:")
 end = st.text_input("Please enter the end nodes separated by spaces:")
 path = nx.dijkstra_path(G, source=start, target=end)
 st.write('Path from node {} to {}:'.format(start, end), path)
 distance = nx.dijkstra_path_length(G, source=start, target=end)
 st.write('The distance from node {} to {} is: '.format(start, end), distance)
 st.write(f"The distance from {start} to {end} is: ...")