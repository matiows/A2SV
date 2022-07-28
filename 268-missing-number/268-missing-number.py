class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        nums.append(0)
        for i in range(len(nums)):
            missing = missing ^ i ^ nums[i]
        return missing