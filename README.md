## What is the worst place in New York City to have a heart attack?
### CS 136 Final Project By Miranda Chaiken and Nick Post

Our question is a variation of the shortest path problem. We wonder, at what point in New York City is a serious medical problem most dangerous? Or, in more concrete terms, what point in New York City is farthest from a hospital?

1. Use the OpenStreetMap API and wget or curl to download the street data for New York City.

2. Download data about hospital locations in New York City https://data.cityofnewyork.us/Health/Health-and-Hospitals-Corporation-HHC-Facilities/f7b6-v6v3

3. Parse the XML data and load it into a graph structure using C++. Store the hospital location nodes separately as the sources for our shortest path calculations.
  * Depending on the size of the data set, we will choose an appropriate scale to call a “node”. Ideally we would use the actual nodes of the graph, street intersections, but if we need to shrink the data set to make the problem more easily computable we could choose to define a node as a city block or some other radius.
4. Implement Dijkstra’s shortest path algorithm in C++.
  * Use the C++ standard library priority queue or create a priority queue wrapper class for the Boost library Fibonacci Heap to speed up the asymptotic running time of Dijkstra’s shortest path algorithm to O(n log n + m) with n the number of vertices and m the number of edges.

5. Run Dijkstra’s shortest path algorithm with each hospital as the source such that when completed we will know the shortest distance from every node to a hospital.
  * Possibly parallelize these calculations in some manner. A queue and rotating the algorithm between sources or calculating the distances for each source in a separate thread are two possibilities.

6. Find the location(s) farthest from a hospital in the city

7. Upload the results to the Google Maps API  (https://developers.google.com/maps/documentation/javascript/examples/layer-heatmap) to generate a heatmap depicting the distance at each point in NYC from a hospital.
