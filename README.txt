Title?!?!?

Our program uses OpenStreetMap geography data and Dijkstra's algorithm
to calculate the distance from a set of source nodes in a graph. Our
motivating question was to determine what areas of a city are underserved
by some service, such as a fire department or emergency room.

To run our program run

python3 Main.py [OSM input file name] [output csv file name] [source node IDs separated by spaces]

For example:

python3 Main.py lower-manhattan.osm.xml lower-manhattan.csv 42436202 42440284


