class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        prefix = [0 for i in range(n + 1)]
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        
        l, r = 0, n
        while l < r:
            mid = l + (r - l + 1) // 2
            
            poss = False
            cur = mid
            while not poss and cur <= n:
                if prefix[cur] - prefix[cur - mid] + k >= mid:
                    ans = max(ans, mid)
                    poss = True
                cur += 1
            if poss:
                l = mid
            else:
                r = mid - 1
                
        return ans
                
                