class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums
        nums.append(1)
        
        @cache
        def topDown(l, r):
            if l > r:
                return 0
            
            ans = 0
            for k in range(l, r+1):
                check = topDown(l, k-1) + (nums[l-1] * nums[k] * nums[r+1]) + topDown(k+1, r)
                ans = max(ans, check)
                
            return ans
        
        return topDown(1, len(nums)-2)
            