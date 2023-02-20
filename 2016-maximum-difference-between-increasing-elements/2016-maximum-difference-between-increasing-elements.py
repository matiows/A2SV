class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minmum = nums[0]
        res = -1
        
        for num in nums:
            if num > minmum:
                res = max(res,num - minmum)
            
            minmum = min(minmum,num)
        
        return res