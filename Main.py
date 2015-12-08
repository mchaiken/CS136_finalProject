# Main script. Loads test xml data into
# a graph and runs our algorithms/data structures.

import Parser
from GraphList import GraphList
import ShortestPath
import sys
import csv

def main(dataFileName, outputFile, output, interactive=False):
    graph = GraphList()
    sources = Parser.loadData(dataFileName, graph)
    ShortestPath.calculateShortestPath(sources, graph)
    outputToCSV(graph, outputFile)
    if (interactive):
        return graph

def outputToCSV(graph, fileName):
    with open(fileName, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "weight", "lattitude", "longitude"])
        for node in graph.nodeIter():
            writer.writerow([node.label(), node.dist(), node.lat, node.lon])


# Function to load data from handmade test files
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
    main(sys.argv[1], sys.argv[2], sys.argv[3])
    
