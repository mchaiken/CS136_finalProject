#include "GraphList.h"

Edge::Edge(int s, int e, int mweight):m_visited(false),m_weight(mweight),start(s),end(e){}

Edge::~Edge(){}

void Edge::visit(){
  m_visited = true;
}

bool Edge::visited()const{
  return m_visited;
}

int Edge::getEnd()const{
  return end;
}

int Edge::getStart()const{
  return start;
} 
GraphList::Node::Node():m_visited(false),m_label(label),m_dist(-1){}
GraphList::Node::Node(int label):m_visited(false),m_label(label),m_dist(-1){
  edgeList = std::vector<Edge>();
}

GraphList::GraphList(){
  m_nodes = std::unordered_map<int, Node>();
}

void GraphList::addNode(int l){
  Node node = Node(l);
  m_nodes.insert({ l, node});
}

void GraphList::addEdge(int n1, int n2, int weight){

  GraphList::Node node1 = m_nodes[n1];
  GraphList::Node node2 = m_nodes[n2];
  node1.edgeList.push_back( Edge(n1,n2,weight) );
  node2.edgeList.push_back( Edge(n2,n1,weight) );

}

void GraphList::vist(int node){
  m_nodes[node].m_visited = true;
}

bool GraphList::visted(int node){
  return  m_nodes[node].m_visited; 
}

int GraphList::getDist(int node){
  return  m_nodes[node].m_dist;
}

std::vector<Edge>& GraphList::getEdges(int node){
  return m_nodes[node].edgeList;
  
}

void GraphList::setDist(int node,int newDist){
  m_nodes[node].m_dist = newDist;
}
 
