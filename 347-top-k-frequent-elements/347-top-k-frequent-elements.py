from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        heap = []
        for key,value in count.items():
            heapq.heappush(heap, (-value, key))
        
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans