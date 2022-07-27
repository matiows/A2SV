class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        
        pivot = start
        start = 0
        end = len(nums) - 1
        
        if target >= nums[pivot] and target <= nums[end]:
            start = pivot
        else:
            end = pivot
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

            