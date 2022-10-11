class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for i in range(n-1)] + [1] for j in range(m-1)]
        grid.append([1 for i in range(n)])

        for i in range(m-2, -1, -1):
            for j in range(n - 2, -1, -1):
                grid[i][j] = grid[i+1][j] + grid[i][j+1]

        return grid[0][0]