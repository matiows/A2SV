class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left = nums[0]
        answer = max(left, nums[1])
        
        for i in range(2, len(nums)):
            left, answer = answer, max(answer, left+nums[i])
        
        return answer