class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        inbound = lambda x, y : 0 <= x < m and 0 <= y < n

        def topDown(row, col):
            if (row, col) in memo:
                return memo[(row, col)]

            if row == m - 1 and col == n - 1:
                return 1

            temp = 0
            down = (row + 1, col)
            right = (row, col + 1)

            if inbound(right[0], right[1]):
                memo[right] = topDown(right[0], right[1])
                temp += memo[right]

            if inbound(down[0], down[1]):
                memo[down] = topDown(down[0], down[1])
                temp += memo[down]

            return temp
        return topDown(0, 0)