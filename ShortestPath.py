# Functions implementing Dijkstra's shortest path algorithm
# for determining the shortest path between a source and all
# Vertices in an undirected, weighted graph.

import PriorityQueue

# Given the label of the source vertex and a graph object,
# calculates the shortest path from the source to all vertices
# and adds the value to the distance attribute on each vertex.
# No return value. Mutates the graph.
def calculateShortestPath(srcLabel, graph):
    unvisited = PriorityQueue()
    
