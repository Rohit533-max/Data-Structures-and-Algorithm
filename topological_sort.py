class graph:
    def __init__(self,vertices):
        self.V = vertices
        self.adj = [[] for i in range(vertices)]

    def add_edge(self,u,v):
        self.adj[u].append(v)       #Directe edge

    def remove_edge(self,u,v):
        self.adj[u].remove(v)

    def dfs(self,node,visited,adj,stack):
        visited[node] =1
        for i in adj[node]:
            if visited[i] != 1:
                self.dfs(i,visited,adj,stack)
        stack.append(node)

    def toposort(self):
        visited = [0]* self.V
        stack = []
        for i in range(self.V):
            if visited[i] == 0:
                self.dfs(i,visited,self.adj,stack)

        while stack:
            print(stack.pop(), end = " ")


g = graph(6)

g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort:")
g.toposort()