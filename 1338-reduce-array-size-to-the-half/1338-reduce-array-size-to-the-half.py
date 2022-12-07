from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        heap = []
        count = Counter(arr)
        for key, value in count.items():
            heappush(heap, (-value, key))
        
        count = 0
        length = len(arr)
        while length > len(arr) // 2:
            temp = heappop(heap)
            length -= (-1 * temp[0])
            count += 1
            
        return count
        