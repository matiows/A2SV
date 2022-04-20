class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        count = nums[-1]
        result = count
        for i in range(len(nums) - 2, -1, -1):
            count = max(count + nums[i], nums[i])
            result = max(result, count)
        return result