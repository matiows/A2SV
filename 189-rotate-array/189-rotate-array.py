class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        length = len(nums)
        temp = []
        
        if k > len(nums):
            k -= (k // len(nums)) * len(nums)
            
        j = length - k
        
        while j < length:
            temp.append(nums[j])
            j += 1
        
        for i in range (length - k -1, -1, -1):
            nums[i+k] = nums[i]
        
        for i in range(len(temp)):
            nums[i] = temp[i]