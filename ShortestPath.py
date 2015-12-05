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
    source  = graph.getNode(srcLabel)
    unvisited.push((0,source))
    while not unvisited.isEmpty():
        currentNode = unvisited.pop()[1]
        currentNode.visit()
        addNeighbors(currentNode, unvisited)
        

def addNeighbors(currentNode, unvisisted):
    for weight, node in currentNode.neighborsIter:
        if unvisited or node.getDist() > weight + currentNode.getDist():
            node.setDist(weight + currentNode.getDist())
            node.visit()
            unvisited.push((node.getDist(), node))
        
