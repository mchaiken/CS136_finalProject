class Edge:
    
    def __init__(self, start, end, weight= None):
        self._start = start
        self._end = end
        self._weight = weight
        self._visited = False
    
    def visit(self):
        self._visited = True

    def visited(self):
        return self._visited

    def getEnd(self):
        return self._end

    def getStart(self):
        return self._start


class GraphList:
    class _Node:
        def __init__(self, label):
            self.label = label
            self._edgeList = []
            
            # We'll probably want to use floats for distances.
            # I just looked it up and Python has infinity (inf) as
            # a valid float value so we can use that to initialize distance.
            self._dist = sys.maxint
            self._visited = False
        
        def label(self):
            return self.label
        
        def visit(self):
            self._visited = True
        
        def visited(self):
            return self._visited
        
        def addEdge(self, e):
            self._edgeList.append(e)
    
    def __init__():
        self.nodeDict = {}
    
    # Mark vertex with label label as “visited” and return previous value of visited flag
    def visit(self, label):
        self._nodeDict[label].vist()
    
    
    # Returns true iff vertex/edge has been visited
    def visited(self, label):
        return self._nodeDict[label].visted()
    
    
    #View of all edges adjacent to vertex with label label
    def getEdgeList(self, label):
        return self._nodeDict[label]._edgeList

    #View of all vertices in graph
    def vertices(self):
        pass
 
    def add(self, label):
        node = GraphList._Node(label)
        self.nodeDict[label] = node
    
    def addEdge(self, here, there, edge_weight=None):
        nodeHere = self.nodeDict[here]
        nodeThere = self.nodeDict[there]
        nodeHere.addEdge( Edge(here, there, edge_weight) )
        nodeThere.addEdge( Edge(there, here, edge_weight) )
    
    # Remove visit
    def reset(self):
        pass
