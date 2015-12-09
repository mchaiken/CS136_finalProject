Where is the worst Place in NYC to have a heart attack?

Our program uses OpenStreetMap geography data and Dijkstra's algorithm
to calculate the distance from a set of source nodes to all other nodes in a graph. 
Our motivating question was to determine what areas of a city are underserved
by some service, such as a fire department or emergency room.

DEPENDENCIES:

We use the graphviz library to produce visualizations of our graph data structures.
Install the graphviz library and all its depnendencies before running our program.

RUN SYNTAX

To run our program run

python3 Main.py [OSM input file name] [output csv file name] [Ouput type (csv or pdf image)]

Then, when prompted, enter the names of the roads that intersect
at the desired source intersections to define the sources for 
Dijkstra's algorithm to run on.

FOR EXAMPLE:

Unzip the included demonstration-data.osm.xml.zip file, then run:

python3 Main.py demonstration-data.osm.xml demo.csv csv

Then, when prompted, enter:

West 14th Street
5th Avenue
end intersection
1st Avenue
East 26th Street
end intersection
done

This will output a CSV result file using our demonstration data set
(a region of lower Manhattan) and two sources at the intersections of
West 14th St and 5th Ave and 1st Ave and East 26th St. 1st Ave and
E 26th St is one of the hospital locations from our full data set.
The other intersection is randomly chosen for demonstration purposes.

Alternatively, to visualize the graph structure run the program with the output
parameter set to "pdf" instead of "csv".
