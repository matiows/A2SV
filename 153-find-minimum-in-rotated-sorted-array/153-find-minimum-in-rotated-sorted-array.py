class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        mid = (start + end) //2
        
        if len(nums) == 1:
            return nums[0]
        
        while start < end:
            if nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
                return nums[mid]
            
            if nums[start] < nums[end] and nums[start] < nums[mid]:
                return nums[start]
            
            if nums[end] < nums[start] and nums[mid] < nums[start]:
                end = mid
                mid = (start + end) //2
            
            elif nums[end] < nums[start] and nums[mid] > nums[start]:
                start = mid
                mid = (start + end) //2
            
            else:
                return nums[end]
                    