"""Topological sort : Ordering of vertices such that every directed edge "U -> v", vertex u comes before v
The topological sort works only on DAG (Directed Acyclic Graphs)"""
#A directed graph is a graph where the edges of the graph must have a direction, Acyclic -> Does't consist any cycle
class graph:
    def __init__(self,vertices):
        self.V = vertices
        self.adj = [[] for i in range(vertices)]

    def add_edge(self,u,v):
        self.adj[u].append(v)       #Directe edge

    def remove_edge(self,u,v):
        self.adj[u].remove(v)
#DFS for topological sort
    def dfs(self,node,visited,adj):
        visited[node] =1
        for i in adj[node]:
            if visited[i] != 1:
                self.dfs(i,visited,adj)
        self.stack.append(node)
#topological sort function which encounter all the disconnected vetices
    def toposort(self):
        visited = [0]* self.V
        self.stack=[]
        for i in range(self.V):
            if visited[i] == 0:
                self.dfs(i,visited,self.adj)

        while self.stack:
            print(self.stack.pop(), end = " ")


g = graph(6)

g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort:")
g.toposort()