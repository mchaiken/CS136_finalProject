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
    return identifyIntersections(ways)

# Prompts the user to define a series of intersections by road names
# and looks the road names up in the ways dict to find their intersecting
# node to use as a source for Dijkstra's algoritm.
def identifyIntersections(ways):
    print("Interactive input for identifying source nodes for calculations")
    print("Enter the names of the roads that intersect at a desired source location")
    print("followed by 'end intersection' for each intersection.")
    print("Enter 'clear' at any point to clear the current intersection entry")
    print("Then enter 'done'.")
    userInput = input("--> ")
    wayNodeSets = []
    sources = []
    while userInput != "done":
        if userInput == "end intersection":
            if len(wayNodeSets) > 1:
                intersection = wayNodeSets.pop().intersection(*wayNodeSets)
                if len(intersection) == 1:
                    sources.append(intersection.pop())
                    wayNodeSets.clear()
                else:
                    print("Intersection underdefined")
        elif userInput == "clear":
            wayNodeSets.clear()
        else:
            # Use sets to allow efficient computing of intersection of possibly
            # several collections. Way node lists should not be too long (generally <
            # 10 nodeIDs) so creating a new set should not be too costly.
            wayNodeList = ways.get(userInput, None)
            if wayNodeList:
                wayNodeSets.append(set(wayNodeList))
            else:
                print("Road not found.")
        userInput = input("--> ")
    return sources


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
