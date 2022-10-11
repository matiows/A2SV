class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        result = []
        n = len(graph) - 1
        
        def dfs(node, path):
            if node == n:
                result.append(path)
            
            verticies = graph[node]
            
            for vertex in verticies:
                dfs(vertex, path + [vertex])
                
        dfs(0, [0])
        
        return result
        