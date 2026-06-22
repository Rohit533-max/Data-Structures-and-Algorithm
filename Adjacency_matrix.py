"""Graph represented as an adjacency matrix."""
class AdjacencyMatrix:
    def __init__(self,vertices):
        self.V = vertices
        self.matrix = [[0]*vertices for _ in range(vertices)]

    def add_edge(self,u,v):
        self.matrix[u][v] =1
        self.matrix[v][u] =1

    def del_edge(self,u,v):
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0

    def has_edge(self,u,v):
        return self.matrix[u][v] ==1
    #standard print function
    # def __str__(self):
    #     return str(self.matrix)
    
    # custom print function
    def __str__(self):
        return "\n".join(str(row) for row in self.matrix)



s = AdjacencyMatrix(5)
s.add_edge(0,1)
s.add_edge(0,2)
s.add_edge(1,3)
print(s.print_matrix())