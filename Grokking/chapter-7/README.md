# Chapter 7: Trees and Graphs

In this chapter, you will learn about trees, the differences between trees and graphs, and how to run algorithms over a tree. You will also explore depth-first search (DFS), breadth-first search (BFS), and Huffman coding, a compression algorithm that utilizes trees.

## Trees vs. Graphs

A **tree** is a special type of graph that has no cycles and is connected. It has a hierarchical structure with a root node and child nodes.

A **graph** is a collection of nodes (vertices) and edges connecting them. Graphs can have cycles and can be either directed or undirected.

## Visual Representation

### Tree

```
Root Node        (A)
                / | \
Parent Nodes (B) (C) (D)
              /    |     \
Child Nodes  (E)  (F)     (G)
             /     |     /  \
Leaf Nodes  (H)   (I)  (J)  (K)
```

### Graph

```
A -- B
|  / |
| /  |
C -- D
```

## Algorithms

### Depth-First Search (DFS)

DFS explores as far as possible along each branch before backtracking.

### Breadth-First Search (BFS)

BFS explores all the nodes at the present depth level before moving on to the nodes at the next depth level.

### Huffman Coding

Huffman coding is a compression algorithm that uses a binary tree to encode data efficiently.

Happy Coding!
