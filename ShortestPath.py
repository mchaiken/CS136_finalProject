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
    while not unvisited.isEmpty():
        print(unvisited.peek()[1])
        currentNode = graph.getNode( unvisited.pop()[1] )
        currentNode.visit()
        addNeighbors(currentNode, unvisited,graph)
        

def addNeighbors(currentNode, unvisited,graph):
    for weight, nodeLabel in currentNode.neighborsIter():
        node = graph.getNode(nodeLabel)
        
        if (not node.visited()) or node.dist() > weight + currentNode.dist():
            node.setDist(weight + currentNode.dist())
            node.visit()
            unvisited.push((node.dist(), node.label()))
        print("NODE "+str(node))
        print("Weight "+str(weight))
