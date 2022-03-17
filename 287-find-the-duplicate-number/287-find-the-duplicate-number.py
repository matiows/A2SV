class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = [0] * (max(nums))
        
        for num in nums:
            counter[num-1] += 1
        
        for i in range(1, len(counter)):
            counter[i] += counter[i-1]
        
        left = 0
        right = len(counter) - 1
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if counter[mid] > mid+1:
                result = mid + 1
                right = mid - 1
                
            else:
                left = mid + 1
                
        return result
                
                