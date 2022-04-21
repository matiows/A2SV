class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if nums[abs(num) -1] > 0:
                nums[abs(num) -1] *= -1
            else:
                result.append(abs(num))
        return result