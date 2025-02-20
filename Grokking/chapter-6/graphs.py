# Learn to model a network using a new, abstract data structure called a graphs.
# Define the graph
graph = {}
graph["Twin Peaks"] = ["walk"] # Twin Peaks is the starting node. It has two neighbors, Walk1 and Walk2.
graph["walk"] = ["Bus #44"] # Walk1 has one neighbor, Bus #44.
graph["Bus #33"] = ["Bus #51"] # Bus #33 has one neighbor, Bus #51.
graph["Bus #33L"] = ["Bus #38"] # Bus #33L has one neighbor, Bus #38.
graph["Bus #38"] = ["Bus #28"] # Bus #38 has one neighbor, Bus #28.
graph["Bus #51"] = ["Bus #28"] # Bus #51 has one neighbor, Bus #28.
graph["Bus #44"] = ["Bus #28"] # Bus #44 has one neighbor, Bus #28.
graph["Bus #28"] = ["Golden Gate Bridge"] # Bus #28 has one neighbor, Golden Gate Bridge.
graph["Golden Gate Bridge"] = [] # Golden Gate Bridge has no neighbors.

# Example graph:
# Twin Peaks -> walk -> Bus #44 -> Bus #28 -> Golden Gate Bridge 2 stops
# Twin Peaks -> walk -> Bus #33L -> Bus #38 -> Bus #28 -> Golden Gate Bridge 3 stops
# Twin Peaks -> walk -> Bus #33 -> Bus #51 -> Bus #28 -> Golden Gate Bridge 3 stops

# Question: what's your algorithm to find the path with the fewest stops?
# Question: what's the shortest path from Twin Peaks to Golden Gate Bridge?
# Question: What do mean by stops in the context of this graph?
# Question: How many Steps are there from Twin Peaks to Golden Gate Bridge?
# Answer: breadth-first search. It's the shortest path algorithm for unweighted graphs.
# Thoughs: Well, can get there in one stop? No. Two stops? Yes. Three stops? Yes. Four stops? No. So, the shortest path is Twin Peaks -> walk -> Bus #44 -> Bus #28 -> Golden Gate Bridge.
# Answer: A stop is a node in the graph. A stop is a place where you can get on or off the bus.
# what is the shortest path from Twin Peaks to Golden Gate Bridge?
# Twin Peaks -> walk -> Bus #44 -> Bus #28 -> Golden Gate Bridge 2 stops in total.
# Answer: 4 steps from Twin Peaks to Golden Gate Bridge. Twin Peaks -> walk -> Bus #44 -> Bus #28 -> Golden Gate Bridge, 5 steps in total from Twin Peaks to Golden Gate Bridge for 2 nodes and 3 edges.

# Another Example graph: friends playing game of poker, who is connected to who?
poker = {} # poker is the name of the graph.
poker ["Alex"] = ['Rama'] # Alex is connected to Rama
poker ['Tom'] = ['Rama', 'Adit'] # Tom is connected to Rama and Adit
poker ['Rama'] = ['Adit'] # Rama is connected to Adit

# Example graph:
# Alex -> Rama
# Tom -> Rama
# Tom -> Adit
# Rama -> Adit

# Question: Who are the people that owes money?
# Answer: Alex  owes Rama money, Tom owes Rama money, Tom owes Adit money, and Rama owes Adit money.
