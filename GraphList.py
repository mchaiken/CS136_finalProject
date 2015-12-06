class Node:
    def __init__(self, label):
        self._label = label
        self._edgeList = []
        
        # Initialize distance to infinity for Dijkstra's algorithm
        self._dist = float("inf")
        
        # Include the label of the source that dist is from
        # to enable running Dijkstra's from multiple sources simulataneously.
        self._srcLabel = None
        self._visited = False
        
    def label(self):
        return self._label

    # Returns a tuple (srcLabel, distance) indicating
    # the current min distance to the node and which source
    # the distance is from.
    def dist(self):
        return self._dist
        
    def setDist(self, dist):
        self._dist = dist

    def visit(self):
        self._visited = True
        
    def visited(self):
        return self._visited
        
    def _addEdge(self, e):
        self._edgeList.append(e)
            
    # A generator to iterate over all nodes adjacent to self.
    def neighborsIter(self):
        for edge in self._edgeList:
            yield (edge._weight, edge.end())
            
    # Returns a collection of all nodes adjacent to self.
    def neighbors(self):
        return [ (edge._weight, edge.end()) for edge in self._edgeList ]
        

class GraphList:
    class _Edge:
    
        def __init__(self, start, end, weight=None):
            self._start = start
            self._end = end
            self._weight = weight
            
        def end(self):
            return self._end
            
        def start(self):
            return self._start
            
            
    def __init__(self):
           self._nodeDict = {}
    
    # Mark node with label label as “visited".
    # Requires the labeled node be in the graph.
    # Throws a KeyError if label is not in the graph.
    def visit(self, label):
        node = self._nodeDict.get(label)
        if node:
            node.visit()
        else:
            raise KeyError("Node not in graph")

    # Returns true iff vertex/edge has been visited.
    # Returns None if label is not in the graph.
    def visited(self, label):
        return self._nodeDict.get(label) and self._nodeDict[label].visted()

    def nodeIter(self):
        for node in self._nodeDict.items():
            yield node[1]
  
    # Return the Node associated with label or None
    # if the label is not in the graph.
    def getNode(self, label):
        return self._nodeDict.get(label)
    
    # Add a new Node with label as its label to the
    # graph. Overwrites any existing Node with the same label.
    def addNode(self, label):
        node = Node(label)
        self._nodeDict[label] = node
        print (self._nodeDict)

    # Add an edge from here to there with optional weight edge_weight to
    # the graph. If here or there is not already in the graph, adds a Node
    # with the proper label to the graph.
    def addEdge(self, here, there, edge_weight=None):
        nodeHere = self._nodeDict.setdefault(here, Node(here))
        nodeThere = self._nodeDict.setdefault(there, Node(there))
        nodeHere._addEdge( GraphList._Edge(here, there, edge_weight) )
        nodeThere._addEdge( GraphList._Edge(there, here, edge_weight) )
    
    # Remove visit
    def reset(self):
        pass
