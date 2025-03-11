import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Define nodes and edges
nodes = [10, 20, 5, 2, 7, 25] # 10 is the root node (No parent)
edges = [(10, 20), (10, 5), (5, 2), (5, 7), (20, 25)]  # (parent, child)

# Add nodes and edges
G.add_nodes_from(nodes)
G.add_edges_from(edges)


# Function to assign levels (depths) to nodes
def assign_levels(graph, root):
    levels = {root: 0}  # Root starts at level 0
    queue = [(root, 0)]  # (node, level)

    while queue:
        node, level = queue.pop(0)
        for child in graph.successors(node):
            if child not in levels:  # Prevent cycles
                levels[child] = level + 1
                queue.append((child, level + 1))

    return levels


# Find root node(s) (nodes with no incoming edges)
root_nodes = [node for node in G.nodes if G.in_degree(node) == 0]

# Assign levels based on first root node
if root_nodes:
    levels = assign_levels(G, root_nodes[0])  # Assuming a single root

    # Set node attributes for layout
    nx.set_node_attributes(G, levels, "subset")

    # Generate a tree-like layout using the assigned levels
    pos = nx.multipartite_layout(G, subset_key="subset")

    # Draw the graph
    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue",
            font_size=15, font_color="black", font_weight="bold", arrows=True)
    plt.show()

else:
    print("No root node found! Ensure the graph is a tree.")
# Output: A tree-like graph with nodes at different levels based on the assigned levels
"""
Root node       (10)
                /  \
Parents node  (20) (5)
              /    / \
Child node  (25) (2) (7) Leaf nodes
"""