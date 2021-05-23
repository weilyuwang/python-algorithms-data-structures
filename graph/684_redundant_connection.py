'''
684. Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 
Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]


Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
'''

from typing import DefaultDict, List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        '''
        For each edge (u, v), traverse the graph with a depth-first search 
        to see if we can connect u to v. If we can, then it must be the duplicate edge.
        
        Time Complexity: O(N^2) where N is the number of vertices 
        (and also the number of edges) in the graph. 
        In the worst case, for every edge we include, 
        we have to search every previously-occurring edge of the graph.
        '''
        graph = DefaultDict(set)
        seen = set()

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target: return True
                return any(dfs(neighbor, target) for neighbor in graph[source])

        for u, v in edges:
            seen.clear() 
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)
