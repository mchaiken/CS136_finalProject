# Functions to parse osm.xml data and create our graph.

from xml.sax import parse
from XMLParseObjects import *
from math import cos, radians, sqrt

def loadData(xmlFile, graph):
    nodes = {}
    ways = {}
    
    firstPassHandler = RelevantDataIdentifier(nodes, ways)
    parse(xmlFile, firstPassHandler)
    
    secondPassHandler = CoordinateGetter(nodes)
    try:
        parse(xmlFile, secondPassHandler)
    except EndOfNodes:
        # Catch exception thrown upon reaching ways section of the file
        # to stop parsing and do nothing.
        pass
    
    populateGraph(nodes, ways, graph)

# Iterate through each way identified as a road in order, identify the
# sections between intersections which will be the edges in our graph,
# calculate the length of the sections, and add them to the graph.
def populateGraph(nodes, ways, graph):
    prevIntersection = None
    prevNode = None
    distance = 0
    for nodeList in ways.values():
        for nodeID in nodeList:
            nodeObj = nodes[nodeID]
            if prevIntersection:
                distance += dist(prevNode, nodeObj)
            if nodeObj.isIntersection():
                if not prevIntersection:
                    prevIntersection = nodeObj
                else:
                    # Check if endpoints of edge are in the graph, if not add them.
                    if prevIntersection.id not in graph:
                        graph.addNode(prevIntersection.id, prevIntersection.lat, prevIntersection.lon)
                    if nodeObj.id not in graph:
                        graph.addNode(nodeObj.id, nodeObj.lat, nodeObj.lon)
                    graph.addEdge(prevIntersection.id, nodeObj.id, distance)
                    prevIntersection = nodeObj
                    distance = 0
            prevNode = nodeObj

        # Clear computation state
        prevIntersection = None
        prevNode = None
        distance = 0

# Calculates the distance between two OSMNode objects in meters
# along the surface of the Earth using the Equirectangular
# approximation which should be sufficient given the relatively
# short distances we are working with.
def dist(nodeObjA, nodeObjB):
    dLat = radians(nodeObjB.lat - nodeObjA.lat)
    dLon = radians(nodeObjB.lon - nodeObjA.lon)
    mLat = radians((nodeObjA.lat + nodeObjB.lat) / 2)
    r = 6371009
    return r * sqrt(dLat**2 + (cos(mLat) * dLon)**2)
