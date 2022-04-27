class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        dp = [1] * len(prices)
        
        for i in range(len(prices) - 1, 0, -1):
            if prices[i] == prices[i - 1] - 1:
                dp[i - 1] = dp[i] + 1
                
        return sum(dp)