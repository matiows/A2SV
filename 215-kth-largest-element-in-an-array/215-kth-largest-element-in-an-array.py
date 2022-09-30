class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        nums.sort()
        
        for num in nums:
            heappush(heap, -num)
        
        for _ in range(k):
            ans = (-1*(heappop(heap)))
            
        return ans