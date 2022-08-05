class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
#   bottom up dp solution 
#   Start by intializing an array with the size of target
#   and build up how many ways there are to get to that target
        dp = [0] * (target + 1)
        
        dp[0] = 1
        for i in range(target + 1):
            for val in nums:
                if val + i <= target:
                    dp[i+val] += dp[i]
        
        
        return dp[-1]