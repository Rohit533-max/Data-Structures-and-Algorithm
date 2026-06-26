# Depth First Search (DFS) Algorithm Implementation
def dfs(node, visited, ans, adj_lis):
    visited[node] =1
    ans.append(node)
    for i in adj_lis[node]:
        if visited[i] != 1:
            dfs(i,visited,ans,adj_lis)

#breadth First Search (BFS) Algorithm Implementation
from collections import deque
def bfs(start,visited,ans,adj_lis):
    q = deque([start])
    visited[start] = 1
    while q:
        node = q.popleft()
        ans.append(node)
        for i in adj_lis[node]:
            if visited[i] ==0:
                q.append(i)
                visited[i] = 1


# n = 8
# visited = [0]*(n+1)
# ans = []
# adj_lis = [[],[2,4],[1,3,6],[2],[1,5,7],[4,8],[2],[4,8],[5,7]]
# dfs(1, visited, ans, adj_lis)
# print(ans)
# bfs(1, visited, ans, adj_lis)