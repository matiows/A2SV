class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.findLeft(nums, target)
        right = self.findRight(nums, target)
        result = [left, right]

        return result
    
    def findLeft(self, nums, target):
        left = 0
        right = len(nums) - 1
        temp = -1

        while left <= right:
            mid =  left + (right -  left) // 2

            if nums[mid] == target:
                temp = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return temp

    def findRight(self, nums, target):
        left = 0
        right = len(nums) - 1
        temp = -1

        while left <= right:
            
            mid =  (right +  left) // 2
            if nums[mid] == target:
                temp = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return temp