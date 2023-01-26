class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(set)
        costs = {}
        visited = set()
        
        for sorc, dest, cost in flights:
            graph[sorc].add(dest)
            costs[(sorc, dest)] = cost
          
        @lru_cache(None)
        def dfs(node, steps):
            if node == dst:
                return 0
                
            if steps < 0:
                return float('inf')
            
            result = float('inf')
            for nei in graph[node]:
                if (node, nei) not in visited:
                    visited.add((node, nei))
                    result = min(result, dfs(nei, steps - 1) + costs[(node, nei)])
                    visited.remove((node, nei))
                
            return result
        
        result = dfs(src, k)
        return result if result != float('inf') else -1
            