"""A adjacency List is used to repersent a graph, where each vertex (or node) stores a list of all its neighbours that are directly connected to it."""

class AdjacencyList:
    def __init__(self,vertices):
        self.V = vertices
        self.adj_list = [[] for i in range(vertices)]
    
    def add_edge(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u) #vice versa for undirected graph

    def del_edge(self,u,v):
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)

    def has_edge(self,u,v):
        return v in self.adj_list[u]
    
    def __str__(self):
        return str(self.adj_list)

# s = AdjacencyList(5)
# s.add_edge(0,1)
# s.add_edge(0,2)
# s.add_edge(1,3)
# s.add_edge(3,4)
# s.del_edge(1,3)

# print(s)
# print(s.has_edge(1,3))