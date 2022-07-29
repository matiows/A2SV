class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        col = [0] * len(grid[0])
        row = [0] * len(grid)
        for i in range(len(grid)):
            row[i] = max(grid[i])
            for j in range(len(grid[0])):
                col[j] = max(col[j], grid[i][j])
                
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total += min(col[j], row[i]) - grid[i][j]
        
        return total