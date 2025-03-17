# All Paths From Source to Target (https://leetcode.com/problems/all-paths-from-source-to-target/)
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        
        # Recrusive func for depth first search to explore paths
        def deep_first_search(node, path):
            # If we are reached the target node(n-1) we add the current path to the result./
            if node == len(graph)-1:
                result.append(path)
                return 
            
            # Exploring all the neighbors of th ecurrent node
            for neighbor in graph[node]:
                # Calling recruise func for depth first search to elpore paths for each neighbor
                deep_first_search(neighbor,path+[neighbor])
        
        # Start deep first search function from 0 node with inital path, which contains only node 0
        deep_first_search(0,[0])
        return result