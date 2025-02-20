# Breath First Search is an Example of search algorithm that uses on a graph.
# Breath First Search is an algorithm for traversing or searching tree or graph data structures.
# It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key') and explores the neighbor nodes at the present depth prior to moving on to nodes at the next depth level.

# Breath First Search has two type of questions:
# 1. Search Questions: Is there a path from A to B?
# 2. Path Questions: What is the shortest path from A to B?

# Let Give you Example of mango problem: On Facebook you have 500 friends, and you want to know who is selling mangoes.
# You can ask your friends, and they can ask their friends
# You can use BFS to find out who is selling mangoes.
# 1. Search Question: Is there a path from A to B?
# 2. Path Question: What is the shortest path from A to B?
# 3. Path Question: What is the shortest path from A to B with the fewest number of stops?


# Let's create a visual representation of the mango selling problem:
#
# You (A) have 10 friends:
# A -> B, C, D, E, F, G, H, I, J, K
#
# Each of your friends has their own friends:
# B -> L, M
# C -> N, O
# D -> P, Q
# E -> R, S
# F -> T, U
# G -> V, W
# H -> X, Y
# I -> Z
# J -> AA, BB
# K -> CC, DD
#
# The goal is to find out who among these friends (or friends of friends) is selling mangoes.
#
# The graph can be visualized as:
#
#        A
#      / | \  \  \  \  \  \  \  \  \  \
#     B  C  D  E  F  G  H  I  J  K
#    /|  |\  |\  |\  |\  |\  |\  |  |  |\
#   L M  N O  P Q  R S  T U  V W  X Y  Z  AA BB  CC DD

from collections import deque

def breadth_first_search(graph, start_node):
    # Create a queue
    queue = deque()
    # Add the starting node to the queue
    queue.append(start_node)
    # Create a list to keep track of visited nodes
    visited = []
    # Loop until the queue is empty
    while queue:
        # Pop the first node from the queue
        node = queue.popleft()
        # Check if the node has already been visited
        if node not in visited:
            # Add the node to the list of visited nodes
            visited.append(node)
            # Add all the neighbors of the node to the queue
            queue.extend(graph[node])
    # Return the list of visited nodes
    return visited

# Define the graph
graph = {}
graph['cab'] = ['cat', 'car'] # cab is the starting node. It has two neighbors, cat and car.
graph['cat'] = ['bat', 'mat'] # cat has two neighbors, bat and mat.
graph['car'] = ['cat', 'bar'] # car has two neighbors, cat and bar.
graph['mat'] = ['bat'] # mat has one neighbor, bat.
graph['bar'] = ['bat'] # bar has one neighbor, bat.
graph['bat'] = [] # bat has no neighbors.

# Find the shortest path from cab to bat
print(breadth_first_search(graph, 'cab')) # ['cab', 'cat', 'car', 'bat', 'mat', 'bar']

