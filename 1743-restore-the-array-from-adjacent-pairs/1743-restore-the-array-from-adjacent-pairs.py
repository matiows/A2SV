class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for a, b in adjacentPairs:
            graph[a].add(b)
            graph[b].add(a)

        start = 0
        for key, val in graph.items():
            if len(val) == 1:
                start = key
                break
				
        original = []
        visited = set()
        
        def dfs(num):
            visited.add(num)
            
            for next_num in graph[num]:
                if next_num not in visited:
                    dfs(next_num)
            
            original.append(num) 
        
        dfs(start)
        
        return original