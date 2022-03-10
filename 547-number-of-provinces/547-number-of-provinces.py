class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            
            visited.add(i)

            for j in range(len(isConnected[i])):
                if j not in visited and i!=j and isConnected[i][j] == 1:
                    dfs(j)
        
        visited = set()
        cnt = 0
        for i in range(len(isConnected)):
            if i not in visited:
                cnt += 1
                dfs(i)
        return cnt