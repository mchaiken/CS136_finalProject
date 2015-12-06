
from xml.sax import ContentHandler


class OSMNode:

    def __init__(self, lat=None, lon=None):
        # Mostly a container class. All attributes will be public
        # to eliminate the need for getters and setters.

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

        # Map of way IDs to lists of nodes that compose the way.
        self._waysDict = waysDict
        
        # Instance variables to use while parsing
        self._currentWay = None
        self._currentWayIsRoad = False
        self._wayNodes = []

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

    def endElement(self, name):
        if name == "way":
            if self._currentWayIsRoad:
                for nodeID in self._wayNodes:
                    self._nodesDict.setdefault(nodeID, OSMNode()).foundOccurence()
                self._waysDict[self._currentWay] = self._wayNodes
                
            self._currentWay = None
            self._wayNodes = []
            self._currentWayIsRoad = False