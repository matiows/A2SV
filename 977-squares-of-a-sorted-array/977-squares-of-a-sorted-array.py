class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        r = len(nums) - 1
        l = r
        f = 0
        ans = [0]*len(nums)
        for num in nums:
            check = num * num
            if num < 0:
                while check < (nums[r] * nums[r]):
                    r -= 1
                    l -= 1
                ans[l] = check
                l -= 1
                f += 1
            else:
                break
        
        if f == len(nums):
            return ans

        for i in range(len(ans)):
            if ans[i] == 0:
                ans [i] = nums[f] * nums[f]
                f += 1
        return ans