class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_inv = -1
        last_min = -1
        last_max = -1
        length = len(nums)
        answer = 0
        
        for r in range(length):
            # print(r, last_min, last_max, last_inv)
            if nums[r] == minK:
                last_min = r
            
            if nums[r] == maxK:
                last_max = r
            
            if nums[r] < minK or nums[r] > maxK:
                last_inv = r
                last_min = -1
                last_max = -1
                
            if last_min > -1 and last_max > -1 and minK <= nums[r] <= maxK:
                idx = min(last_min, last_max)
                value = idx - last_inv
                answer += value
            # print(answer)  
        return answer
                