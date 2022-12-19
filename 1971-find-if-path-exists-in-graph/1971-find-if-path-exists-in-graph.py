class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        
        for vertex1, vertex2 in edges:
            graph[vertex1].append(vertex2)
            graph[vertex2].append(vertex1)
            
        seen = [False] * n
        seen[source] = True
        queue = deque()
        queue.append(source)
        
        while queue:
            node = queue.popleft()
            
            if node == destination:
                return True
            
            for next_node in graph[node]:
                if not seen[next_node]:
                    seen[next_node] = True
                    queue.append(next_node)

        return False