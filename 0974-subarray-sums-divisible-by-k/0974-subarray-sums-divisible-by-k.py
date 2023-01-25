class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder = defaultdict(int)
        total, count = 0, 0
        remainder[0] = 1
        
        for num in nums:
            total += num
            total %= k
            
            count += remainder[total]
            remainder[total] += 1
            
        return count
        