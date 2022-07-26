class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            if nums[i] not in num_map:
                num_map[target - nums[i]] = i
            else:
                return num_map[nums[i]], i
            