# Functions implementing Dijkstra's shortest path algorithm
# for determining the shortest path between a source and all
# Vertices in an undirected, weighted graph.

from PriorityQueue import *

# Given a list of labels of source nodes and a graph object,
# calculates the shortest path from a source to all nodes
# and adds the value to the distance attribute on each node.
# No return value. Mutates the graph.

#PostCond: Applies a modified Dijkstra's shortest path algorithm 
#          to a given graph for all sources in srcList
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
        # Because nodes may be in multiple source priority queues
        # need to check to make sure min is unvisited, if not pop until
        # it is unvisited.
        while not srcPQ.isEmpty() and currentNode.visited():
            currentNode = graph.getNode(srcPQ.pop())
        currentNode.visit()
        _checkNeighbors(currentNode, srcPQ, graph)
        while not srcPQ.isEmpty() and graph.getNode(srcPQ.peek()).visited():
            srcPQ.pop()
        if not srcPQ.isEmpty():
            sources.push(srcPQ.peekWeight(), srcPQ)
        
#PostCond: looks at neighbors, modifies weights, and if unvisited adds to PriorityQueue
def _checkNeighbors(currentNode, unvisited, graph):
    for weight, nodeLabel in currentNode.neighborsIter():
        node = graph.getNode(nodeLabel)
        if  node.dist() > weight + currentNode.dist():
            node.setDist(weight + currentNode.dist())
        if not node.visited():
            unvisited.push(node.dist(), node.label())
