class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        _min = 1
        _max = 1
        
        for val in nums:
            temp = val * _max
            _max = max(temp, val*_min, val)
            _min = min(temp, val*_min, val)
            result = max(_max, result)
        return result