class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(lambda : defaultdict(set))
        
        for st, en in redEdges:
            graph[st][True].add(en)
            
        for st, en in blueEdges:
            graph[st][False].add(en)
            
        res = [-1] * n
        
        queue = deque([(0,True), (0,False)])
        visited = set([(0,True), (0,False)])
        count = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                node, color = queue.popleft()
                if res[node] == -1:
                    res[node] = count
                else:
                    res[node] = min(res[node], count)
                    
                children = graph[node][not color]
                for child in children:
                    if (child, not color) not in visited:
                        visited.add((child, not color))
                        queue.append((child, not color))
            count += 1
            
        return res