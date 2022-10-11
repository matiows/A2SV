class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        if grid[m-1][n-1] == 1:
            return 0
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m -1 and j == n - 1:
                    grid[i][j] = 1
                    continue

                if grid[i][j] != 1:
                    if i + 1 < m:
                        grid[i][j] += grid[i + 1][j]
                    if j + 1 < n:
                        grid[i][j] += grid[i][j + 1]
                else:
                    grid[i][j] = 0
        return grid[0][0]