class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        graph = defaultdict(set)
        
        for idx, route in enumerate(routes):
            for stop in route:
                graph[stop].add(idx)
                
        queue = deque([[source, 0]])
        visited = set([source])
        
        while queue:
            stop, count = queue.popleft()
            
            if stop == target:
                return count
            
            for idx in graph[stop]:
                for stop in routes[idx]:
                    
                    if stop not in visited:
                        queue.append([stop, count + 1])
                        visited.add(stop)
               
                routes[idx] = []
        
        return -1