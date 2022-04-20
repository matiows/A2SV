class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        self.count = nums[-1]
        self.result = self.count
        def chala(i):
            if i < 0:
                return self.result
            self.count = max(self.count + nums[i], nums[i])
            self.result = max(self.count, self.result)
            return chala(i - 1)
        return chala(len(nums)-2)
            