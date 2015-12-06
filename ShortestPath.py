# Functions implementing Dijkstra's shortest path algorithm
# for determining the shortest path between a source and all
# Vertices in an undirected, weighted graph.

from PriorityQueue import *

# Givenn a list of labels of source nodes and a graph object,
# calculates the shortest path from a source to all nodes
# and adds the value to the distance attribute on each node.
# No return value. Mutates the graph.

def calculateShortestPath(srcList, graph):
    sources = PriorityQueue()

    for src in srcList:
        pq = PriorityQueue()
        pq.push(0, src)
        sources.push(0, pq)
        graph.getNode(src).setDist(0)
    
    while not sources.isEmpty():
        srcPQ = sources.pop()
        currentNode = graph.getNode(srcPQ.pop())
        if currentNode.visited():
            currentNode = graph.getNode(srcPQ.pop())
        currentNode.visit()
        checkNeighbors(currentNode, srcPQ, graph)
        if not srcPQ.isEmpty():
            if srcPQ.peek().visited():
                srcPQ.pop()
            sources.push(srcPQ.peekWeight(), srcPQ)
        

def checkNeighbors(currentNode, unvisited, graph):
    for weight, nodeLabel in currentNode.neighborsIter():
        node = graph.getNode(nodeLabel)
        if  node.dist() > weight + currentNode.dist():
            node.setDist(weight + currentNode.dist())
        if not node.visited():
            unvisited.push((node.dist(), node.label()))

