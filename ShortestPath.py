# Functions implementing Dijkstra's shortest path algorithm
# for determining the shortest path between a source and all
# Vertices in an undirected, weighted graph.

from PriorityQueue import *

# Given the label of the source vertex and a graph object,
# calculates the shortest path from the source to all vertices
# and adds the value to the distance attribute on each vertex.
# No return value. Mutates the graph.

def calculateShortestPath(srcLabel, graph):
    unvisited = PriorityQueue()
    unvisited.push((0,srcLabel))
    graph.getNode(srcLabel).setDist(0)
    while not unvisited.isEmpty():
        currentNode = graph.getNode( unvisited.pop()[1] )
        currentNode.visit()
        checkNeighbors(currentNode, unvisited,graph)
        

def checkNeighbors(currentNode, unvisited,graph):
    for weight, nodeLabel in currentNode.neighborsIter():
        node = graph.getNode(nodeLabel)
        if  node.dist() > weight + currentNode.dist():
            node.setDist(weight + currentNode.dist())
        if not node.visited():
            unvisited.push((node.dist(),node.label()))

