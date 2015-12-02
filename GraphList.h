#ifndef GraphList_h
#define GraphList_h
#include <cstdio>
#include <unordered_map>
#include <vector>

class Edge{
 private:
    bool m_visited;
    const int m_weight;
    const int start;
    const int  end;
    
 public:
    Edge(int s, int e, int mweight);
    ~Edge();
    void visit();
    bool visited()const;
    int getEnd()const;
    int getStart()const; 
};



class GraphList{
 private:

  class Node{
    
  public:
    bool m_visited;
    const int m_label;
    int m_dist;
    std::vector<Edge> edgeList; //linked list in future
    Node(int label);
    ~Node();
  
  };



 public:
  GraphList();
  std::unordered_map<int,Node>  m_nodes; 
  void addNode(int label);

  void addEdge(int n1, int n2,  int weight);

  void vist(int Node);

  bool visted(int Node);


  int getDist(int Node);

  std::vector<Edge>& getEdges(int Node);
  void setDist(int Node,int newDist);
  
};

#endif
