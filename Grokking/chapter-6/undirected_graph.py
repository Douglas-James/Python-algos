import networkx as nx
import matplotlib.pyplot as plt

# Define the graph as a dictionary
graph = {
    "wake up": ["exercise", "eat breakfast", "pack lunch"],
    "exercise": ["shower"],
    "shower": ["get dressed"],
    "get dressed": [],
    "eat breakfast": ["brush teeth"],
    "brush teeth": [],
    "pack lunch": []
}

# Create an undirected graph
G = nx.Graph(graph)

# Define node positions for better visualization
pos = {
    "wake up": (0, 3), "exercise": (-1, 2), "shower": (-1, 1), "get dressed": (-1, 0),
    "eat breakfast": (1, 2), "brush teeth": (1, 1), "pack lunch": (2, 3)
}

# Draw the graph
plt.figure(figsize=(8, 5))
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="black",
        node_size=2000, font_size=10, font_weight="bold")
plt.title("Task Dependency Graph (Undirected)")
plt.show()
