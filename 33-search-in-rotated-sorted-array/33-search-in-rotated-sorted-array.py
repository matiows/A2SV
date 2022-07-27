class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            
            if nums[start] <= nums[mid]:
                if target < nums[start] or target > nums[mid]:
                    start = mid+1
                else:
                    end = mid
            else:
                if target > nums[end] or target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid
        return -1