class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        pointer = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[pointer] = nums[pointer], nums[i]
                pointer += 1