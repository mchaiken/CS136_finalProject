# Testing main script. Loads test xml data into
# a graph and tests our algorithms/data structures.

import xml.etree.ElementTree as et
from GraphList import *
from ShortestPath import *
import sys

def main(dataFileName, interactive=False):
    graph = GraphList()
    loadData(dataFileName, graph)
    if (interactive):
        return graph
    calculateShortestPath(1,graph)
    for node in graph.nodeIter():
        print(str(node.label())+ " -- "+str(node.dist()))
def loadData(fileName, graph):
    tree = et.parse(fileName)
    root = tree.getroot()
    for elem in root.iter("*"):
        if elem.tag == "node":
            # Add node
            graph.addNode(int(elem.get("id")))
        elif elem.tag == "edge":
            # Add edge
            graph.addEdge(int(elem.get("here")), int(elem.get("there")), 
                          float(elem.get("weight")))

if __name__ == '__main__':
    main(sys.argv[1])
    
