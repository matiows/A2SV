class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)
        
        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1/v))

        def dfs(node, div, visited):
            if node not in graph or div not in graph:
                return -1

            if node == div:
                return 1.0

            for neighbor, value in graph[node]:
                
                if neighbor not in visited:
                    temp = dfs(neighbor, div, visited | {neighbor})
                    if temp != -1:
                        return value * temp

            return -1

        answer = []
        for n, d in queries:
            answer.append(dfs(n, d, set()))
            
        return answer