# Main script. Loads test xml data into
# a graph and runs our algorithms/data structures.

import Parser
from GraphList import GraphList
import ShortestPath
from graphviz import Graph
import sys
import csv

#PreCond: dataFileName exists, and contains valid OpenStreetMap (OSM) XML
#PostCond: Reads in datafile, parses, loads into graph and writes output to CSV or PDF
def main(dataFileName, outputFile, outputType):
    graph = GraphList()
    sources = Parser.loadData(dataFileName, graph)
    if outputType=="csv":
        ShortestPath.calculateShortestPath(sources, graph)
        outputToCSV(graph, outputFile)
    else: 
        outputToPdf(graph, outputFile, sources)

#PostCond: Outputs nodes and weights to CSV after running Dijkstra
def outputToCSV(graph, fileName):
    with open(fileName, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "weight", "lattitude", "longitude"])
        for node in graph.nodeIter():
            writer.writerow([node.label(), node.dist(), node.lat, node.lon])

#PostCond: Draws graph to a pdf using graphviz instead of running Dijkstra
#Just for display purposes 
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
    
    

if __name__ == '__main__':
    #Command-line arguments: file to read in, file to read out to, whether to output to a CSV or a graph
    main(sys.argv[1], sys.argv[2], sys.argv[3])
