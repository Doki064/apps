import streamlit as st
import os
import sys
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
def app():
 # Define the number of nodes
 nodes = np.array(["v1", "v2", "v3", "v4", "v5","a6","b7","c8","b9","c10"])
 # Define the distance between nodes
 row = np.array(["v1", "v1", "v5", "a6", "a6", "c8", "v1", "b9", "a6", "v4","v2","v1","v2","b7","c8","b7","b9"])
 col = np.array(["c10", "v3", "v3", "v5", "c8", "c10", "b9", "a6", "v4", "v1","b9","c8","b7","v3","v4","v5","v3"])
 value = np.array([2.6, 5.2, 2.7, 3.8, 1.5, 9.1, 10, 8.3, 6.2, 7, 2.3,3.7,11, 13.2, 9.8, 7.4, 5.5])
 # Generate undirected graph
 G = nx.Graph()
 # Add a node to the graph
 for i in range(0, np.size(nodes)):
    G.add_node(nodes[i])
 # Add weighted edges
 for i in range(0, np.size(row)):
    G.add_weighted_edges_from([(row[i], col[i], value[i])])
 # Set network layout
 pos = nx.shell_layout(G)
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