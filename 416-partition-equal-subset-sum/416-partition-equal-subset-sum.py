class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # parttion into 2 subsets
        # so total sum = 2 * subset sum
        # total sum needs to be even
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        dp = {}
        dp[(0, 0)] = True
        def check(index, s):
            if s == 0:
                return True
            if index == len(nums) or s < 0:
                return False
            if (index, s) in dp:
                return dp[(index, s)]
            dp[(index, s)] = check(index + 1, s) or check(index + 1, s - nums[index])
            return dp[(index, s)]
        return check(0, subset_sum)
        