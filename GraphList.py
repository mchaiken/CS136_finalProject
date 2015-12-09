#Public node class to allow direct manipulation of Nodes in Dijkstra
class Node:
    
    def __init__(self, label, lat, lon):
        self._label = label
        self._edgeList = []
        
        # lat, lon intentionally public to avoid writing simple getter/setter methods
        self.lat = lat
        self.lon = lon

        # Initialize distance to infinity for Dijkstra's algorithm
        self._dist = float("inf")
        
        # Include the label of the source that dist is from
        # to enable running Dijkstra's from multiple sources simulataneously.
        self._srcLabel = None
        self._visited = False

    def label(self):
        return self._label
    
    def dist(self):
        return self._dist
    
    def setDist(self, dist):
        self._dist = dist
    
    def visit(self):
        self._visited = True
    
    def visited(self):
        return self._visited

    #PostCond: Adds edge to this nodes edgeList
    def _addEdge(self, e):
        self._edgeList.append(e)
            
    #PostCond: A generator to iterate over all nodes adjacent to self.
    def neighborsIter(self):
        for edge in self._edgeList:
            yield (edge._weight, edge.end())
            
    #PostCond: Returns a collection of all nodes adjacent to self.
    def neighbors(self):
        return [ (edge._weight, edge.end()) for edge in self._edgeList ]
        
#Undirected GraphList Class containing private edge class,
#Contains no methods for removing edges or nodes from the graph
class GraphList:
    
    #Private edge class. Edges are directed but graph is not
    class _Edge:
        def __init__(self, start, end, weight=None):
            self._start = start #Start node of edge 
            self._end = end #end node of edge
            self._weight = weight #length of edge
            
        def end(self):
            return self._end
            
        def start(self):
            return self._start
            
            
    def __init__(self):
        #Dictionary of all nodes in Graph with key as int node ID
        self._nodeDict = {} 
           
    #PreCond: Requires the labeled node be in the graph.
    #PostCond:  Mark node with label label as "visited"
    # Throws a KeyError if label is not in the graph.
    def visit(self, label):
        node = self._nodeDict.get(label)
        if node:
            node.visit()
        else:
            raise KeyError("Node not in graph")

    #PostCond: Returns true iff vertex/edge has been visited.
    # Returns None if label is not in the graph.
    def visited(self, label):
        return self._nodeDict.get(label) and self._nodeDict[label].visted()

    def nodeIter(self):
        for node in self._nodeDict.values():
            yield node
  
    #PostCond: Return the Node associated with label or None
    # if the label is not in the graph.
    def getNode(self, label):
        return self._nodeDict.get(label)
    
    #PostCond: Overload in operator to allow checking if a node is in the graph.
    # Hashmap lookup, so O(1).
    def __contains__(self, label):
        return label in self._nodeDict

    #Post Cond: Add a new Node with label as its label to the
    # graph. Overwrites any existing Node 
    # with the same label.
    def addNode(self, label, lat, lon):
        self._nodeDict[label] = Node(label, lat, lon)

    #PreCond: Nodes labels (here and there) are already in the graph.
    #PostCond: Add an edge from here to there with optional weight edge_weight to
    # the graph. 
    def addEdge(self, here, there, edge_weight=None):
        assert here in self._nodeDict
        assert there in self._nodeDict
        self._nodeDict[here]._addEdge( GraphList._Edge(here, there, edge_weight) )
        self._nodeDict[there]._addEdge( GraphList._Edge(there, here, edge_weight) )
