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
                    if i in memo:
                        count = max(count, memo[i] + 1)
                    else:
                        count = max(count, dp(i) + 1)
             
            memo[index] = count
            return memo[index]
        answer = 1
        for i in range(len(nums)):
            if i in memo:
                answer = max(answer, memo[i])
            else:
                answer = max(answer, dp(i))
        return answer