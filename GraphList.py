
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
    
    # Mark vertex with label label as “visited” and return previous value of visited flag
    def visit(self, label):
        self._nodeDict[label].vist()
    
    # Returns true iff vertex/edge has been visited
    def visited(self, label):
        return self._nodeDict[label].visted()

    def getNode(self, label):
        return self._nodeDict(label)
 
    def addNode(self, label):
        node = Node(label)
        self._nodeDict[label] = node
    
    def addEdge(self, here, there, edge_weight=None):
        nodeHere = self._nodeDict.setDefault(here, Node(here))
        nodeThere = self._nodeDict.setDefault(there, Node(there))
        nodeHere._addEdge( _Edge(here, there, edge_weight) )
        nodeThere._addEdge( _Edge(there, here, edge_weight) )
    
    # Remove visit
    def reset(self):
        pass
