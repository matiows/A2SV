class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_prefix = [0]
        right_prefix = [0]
        for i in range(len(nums)-1,-1,-1):
            right_prefix.append(right_prefix[-1] + nums[i])

        leftSum = 0
        for i in range(len(nums)):
            if leftSum == right_prefix[len(nums) - i - 1]:
                return i
            leftSum += nums[i]
        return -1