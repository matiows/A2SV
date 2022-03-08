import heapq as h

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        h.heapify(self.heap)

    def add(self, val: int) -> int:
        h.heappush(self.heap, val)
        
        while len(self.heap) > self.k:
            h.heappop(self.heap)
            
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)