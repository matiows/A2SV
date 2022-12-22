class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        memo = {}
        
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
            
        visited = [False] * n
        
        def calculate(node):
            visited[node] = True
            node_dist = node_size = 0
            
            for nei in graph[node]:
                if not visited[nei]:
                    dist, no_nodes = calculate(nei)
                    node_dist += dist
                    node_size += no_nodes 
                   
            memo[node] = (node_dist + node_size, node_size)
            return node_dist + node_size, node_size + 1
                    
        calculate(0)
        
        answer = [0] * n
        visited = [False] * n

        def find(node):
            visited[node] = True
            
            for nei in graph[node]:
                if not visited[nei]:
                    dist, nodes = memo[node]
                    my_dist, my_nodes = memo[nei]

                    value = dist - (my_nodes + 1)
                    value += n - (my_nodes + 1)

                    memo[nei] = value, my_nodes
                    answer[nei] = value

                    find(nei)
                    
        find(0)
        answer[0] = memo[0][0]
        return answer  
        