class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        _sum = sum(nums)
        leftsum = 0
       
        for i in range(len(nums)):
            if leftsum == _sum - leftsum - nums[i]:
                return i
            leftsum += nums[i]
        return -1
    