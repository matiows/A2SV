class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        _max = 1
        
        for i in range(1, n+1):
            if _max * 2 == i:
                _max = i
            dp[i] = 1 + dp[i - _max]
        return dp