class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        if n < 2:
            return [[1]]
        dp = [[]] * (n+1)
        dp[1] = [1]
        dp[2] = [1,1]
        for i in range(3, n+1):
            dp[i] = [1] * i
            for j in range(1,i-1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp[1:]