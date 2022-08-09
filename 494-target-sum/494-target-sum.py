class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dp(idx, t):
            if (idx, t) in memo:
                return memo[(idx, t)]
            if idx == len(nums):
                if t == 0:
                    return 1
                else:
                    return 0
            
            memo[(idx, t)] = dp(idx + 1, t - nums[idx]) + dp(idx + 1, t + nums[idx])
            return memo[(idx, t)]
        memo = {}
        return dp(0, target)