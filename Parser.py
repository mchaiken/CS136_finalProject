# Functions to parse osm.xml data and create our graph.

from xml.sax import parse
from XMLParseObjects import *

def loadData(xmlFile, graph=None):
    nodes = {}
    ways = {}
    firstPassHandler = RelevantDataIdentifier(nodes, ways)
    parse(xmlFile, firstPassHandler)
    return (nodes, ways)
