"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

""" Leetcode problem 133
1. Using a dictionary to store the orignal and its clone
2. Creating the clone same as the original node
3. Immediately store it in the clone dictionary because if graph has a cycle it will recreate the same val and struck in infinite recursion loop 
4. BASE CASE -> if we found the same value return that clone value to reuse it
5. Looping through all the neighbors and appending them in the copy neighbors by appling dfs on current neighbour"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {}
        def dfs(node):
            if node in clone:
                return clone[node]
            copy = Node(node.val)
            clone[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy
        if node:
            return dfs(node)
        else:
            return 
        
