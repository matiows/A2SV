class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMostk(k):
            left, result = 0, 0
            count = defaultdict(int)
            
            for right, n in enumerate(nums):
                count[n] = count[n] + 1
                k -= count[n] == 1
                
                while left <= right and k < 0:
                    count[nums[left]] -= 1
                    k += count[nums[left]] == 0
                    left += 1
                
                result += (right - left + 1)
            
            return result
        
        return atMostk(k) - atMostk(k-1)