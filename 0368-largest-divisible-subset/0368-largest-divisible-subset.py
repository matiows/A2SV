from collections import deque

class Solution:
    def dp(self, index, nums, memo):
        length = len(nums)
        
        if index == length - 1:
            return [nums[index]]
        
        if index in memo:
            return memo[index]
        
        array = []
        for i in range(index + 1, length):
            
            if nums[i] % nums[index] == 0 or nums[index] % nums[i] == 0:
                
                check_array = self.dp(i, nums, memo)
                
                if len(check_array) > len(array):
                    array = check_array
        
        memo[index] = array + [nums[index]]
        return memo[index]
        
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        answer = []
        memo = {}
        for index in range(len(nums)):
            check = self.dp(index, nums, memo)
            
            if len(check) > len(answer):
                answer = check
        
        return answer