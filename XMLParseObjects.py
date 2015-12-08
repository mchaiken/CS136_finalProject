# Objects used to parse osm.xml input data. A Node container class to help
# store data and two ContentHandler objects to pass to the Python SAX XML
# parser to handle the data as it is read.

from xml.sax import ContentHandler


class OSMNode:

    def __init__(self, id, lat=None, lon=None):
        # Mostly a container class. All attributes will be public
        # to eliminate the need for getters and setters.

        self.id = id
        # Number of times the osm node appears in a way
        self.count = 0
        self.lat = lat
        self.lon = lon

    def foundOccurence(self):
        self.count += 1

    def isIntersection(self):
        return self.count > 1

class RelevantDataIdentifier(ContentHandler):

    _notRoads = ["footway", "cycleway", "path", "service", "track", "pedestrian", "steps"]

    def __init__(self, nodesDict, waysDict):
        super().__init__()
        # Dicts are passed by reference and used to store ouput.

        # Map of node IDs to OSMNode objects to store count and on the next pass
        # lon, lat data.
        self._nodesDict = nodesDict

        # Map of way names to lists of nodes that compose the way.
        self._waysDict = waysDict
        
        # Instance variables to use while parsing
        self._currentWay = None
        self._currentWayIsRoad = False
        self._wayNodes = []
        self._wayName = None

    def startElement(self, name, attrs):
        if name == "way":
            self._currentWay = attrs.getValue("id")
        elif name == "nd":
            if self._currentWay:
                self._wayNodes.append(attrs.getValue("ref"))
        elif name == "tag":
            if (attrs.getValue("k") == "highway" and 
                attrs.getValue("v") not in RelevantDataIdentifier._notRoads):
                self._currentWayIsRoad = True
            elif attrs.getValue("k") == "name":
                self._wayName = attrs.getValue("v")

    def endElement(self, name):
        if name == "way":
            if self._currentWayIsRoad:
                wayDictNodes = self._waysDict.setdefault(self._wayName or self._currentWay, [])
                for nodeID in self._wayNodes:
                    self._nodesDict.setdefault(nodeID, OSMNode(nodeID)).foundOccurence()
                    if nodeID not in wayDictNodes:
                        wayDictNodes.append(nodeID)
                
            # Clear status variables
            self._currentWay = None
            self._wayNodes = []
            self._currentWayIsRoad = False
            self._wayName = None

# Exception to be raised in CoordinateGetter to abort
# SAX parsing upon reaching the ways section of the OSM.xml
# file. Nodes are guaranteed to appear before ways in OSM.xml
# files and on the second pass through the file all we need to
# do is pull out the coordinates of the nodes we identified in the first
# pass, therefore we can save time/space by halting parsing early. 
class EndOfNodes(Exception):
    
    def __init__(self):
        pass

    def __str__(self):
        return "Reached the end of nodes section of OSM.xml file"

class CoordinateGetter(ContentHandler):

    def __init__(self, nodesDict):
        super().__init__()

        # Map of node IDs to OSMNode objects to store count and lon, lat data.
        self._nodesDict = nodesDict

    def startElement(self, name, attrs):
        if name == "node":
            nodeObj = self._nodesDict.get(attrs.getValue("id"))
            if nodeObj:
                nodeObj.lon = float(attrs.getValue("lon"))
                nodeObj.lat = float(attrs.getValue("lat"))
        if name == "way":
            raise EndOfNodes()
