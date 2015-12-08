# Main script. Loads test xml data into
# a graph and runs our algorithms/data structures.

import Parser
from GraphList import GraphList
import ShortestPath
from graphviz import Graph
import sys
import csv


def main(dataFileName, outputFile, outputType):
    graph = GraphList()
    sources = Parser.loadData(dataFileName, graph)
    if outputType=="csv":
        ShortestPath.calculateShortestPath(sources, graph)
        outputToCSV(graph, outputFile)
    else: 
        outputToPdf(graph, outputFile, sources)

def outputToCSV(graph, fileName):
    with open(fileName, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "weight", "lattitude", "longitude"])
        for node in graph.nodeIter():
            writer.writerow([node.label(), node.dist(), node.lat, node.lon])

def outputToPdf(graph, fileName,sourceLables):
    e = Graph('NYC', filename=fileName, engine='dot')
    e.body.extend(['rankdir=LR', 'size="100,100"'])
    e.attr('node', shape='ellipse')
    e.attr("node",color='green', style='filled')
    edgeExists={}
    for label in sourceLables:
        e.node(str(label))
    e.attr("node",color='lightblue2', style='filled')
    for node in graph.nodeIter():
        for edge in node.neighborsIter():
            if not edge[1] in edgeExists:
                e.attr("edge",labelcolor="blue")
                e.edge(str(node.label()),edge[1],str(int(edge[0]))+"m")
        edgeExists[node.label()]=1
    edgeExists=None

    e.body.append(r'label = "\nIntersections in New York City\n"')
    e.body.append('fontsize=100')
    e.view()
    
        

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
