# Graph of topological sort
# graph = {}
# graph["wake up"] = ["get dressed", "eat breakfast", "pack lunch"] # Wake up should come before getting dressed, eating breakfast, and packing lunch
# graph["get dressed"] = ["shower", "exercise"]  # Shower should come before getting dressed
# graph["eat breakfast"] = ["brush teeth"] # Brush teeth should come after eating breakfast
# graph["pack lunch"] = []  # Pack lunch should come after eating breakfast
# graph["shower"] = []  # Shower should come before getting dressed
# graph["exercise"] = [] # Exercise should come before getting dressed
# graph["brush teeth"] = [] # Brush teeth should come after eating breakfast

# Topological sort
familyTree = {}
familyTree["you"] = ["Mom", "Dad"]
familyTree["Mom"] = ["Grandma", "Grandpa"]
familyTree["Dad"] = ["Grandma", "Grandpa"]
familyTree["Grandma"] = []
familyTree["Grandpa"] = []




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

# define the graph as a dictionary
# This graph represents the family tree of a person
# The person has two parents, four grandparents, and eight great-grandparents
# The person is at the root of the tree
# The parents are the children of the person
# The grandparents are the children of the parents  (two grandparents per parent)
# The great-grandparents are the children of the grandparents (two great-grandparents per grandparent)
# The great-grandparents are the leaf nodes of the tree (they have no children)
# The goal is to find the shortest path from the person to the great-grandparents
# The graph can be visualized as:
#
#        you
#      /      \
#    Mom       Dad
#    / \       /  \
#  Alex Sara John Jane
#
familyTrees = {
    "you": ["Mom", "Dad"],
    "Mom": ["Alex", "Sara"],
    "Dad": ["John", "Jane"],
    "Alex": [],
    "Sara": [],
    "John": [],
    "Jane": []


}

# Create a directed graph
G = nx.DiGraph(familyTrees)

# Define node positions for better visualization
pos = {
    "you": (0, 0),
    "Mom": (-1, -1),
    "Dad": (1, -1),
    "Alex": (-2, -2),
    "Sara": (0, -2),
    "John": (1, -2),
    "Jane": (2, -2)
}

# Draw the graph
plt.figure(figsize=(8, 5))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=20, font_weight="bold", arrowsize=10)
plt.title("Family Tree")
plt.show()
# Create a directed graph
