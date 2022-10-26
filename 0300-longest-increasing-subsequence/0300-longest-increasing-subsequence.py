class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dp(index):
            if index == len(nums) - 1:
                return 1
            
            if index in memo:
                return memo[index]
            
            count = 1
            for i in range(index + 1, len(nums)):
                if nums[i] > nums[index]:
                    count = max(count, dp(i) + 1)
             
            memo[index] = count
            return memo[index]
        
        answer = 1
        for i in range(len(nums)):
            answer = max(answer, dp(i))
        return answer