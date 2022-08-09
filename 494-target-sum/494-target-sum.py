class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = {}
        dp[0] = 1
        
        for num in nums:
            newSet = defaultdict(int)
            
            for d in dp:
                newSet[d + num] += dp[d]
                newSet[d - num] += dp[d]
            dp = newSet
        
        return dp[target]