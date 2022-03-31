class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def detonates(b1,b2):
            return (b1[0]-b2[0]) ** 2 + (b1[1]-b2[1]) ** 2 <= b1[2] **2
        
        graph = defaultdict(list)
        
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j and detonates(bombs[i],bombs[j]):
                    graph[i].append(j)
        
        def dfs(n, visited):
            count = 1
            for ne in graph[n]:
                if ne not in visited:
                    visited.add(ne)
                    count += dfs(ne,visited)
            return count
        
        ans = 1
        for idx,bomb in enumerate(bombs):
            visited = set([idx])
            count = dfs(idx,visited)
            ans = max(ans,count)
        
        return ans