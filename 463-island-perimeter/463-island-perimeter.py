class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        perimeter = 0
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))

        def in_bound(row, col):
            return 0 <= row < n and 0 <= col < m

        def dfs(row, col):
            side = 0
            for dr, dc in directions:
                nrow, ncol = row + dr, col + dc
                if not in_bound(nrow, ncol) or grid[nrow][ncol] == 0:
                    side += 1

            return side
        
        
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    perimeter += dfs(row, col)
        return perimeter
