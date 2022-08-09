class Solution:
    def minSteps(self, n: int) -> int:
        def dp(cnt,clipboard):
            if (cnt, clipboard) in memo:
                return memo[(cnt, clipboard)]
            if cnt == n:
                return 0
            
            if cnt > n:
                return float('inf')
            
            memo[(cnt, clipboard)] = min(1 + dp(cnt + clipboard, clipboard),
            2 + dp(cnt * 2, cnt))
            return memo[(cnt, clipboard)]
        
        if n == 1:
            return 0
        memo = {}
        return dp(2, 1) + 2
        