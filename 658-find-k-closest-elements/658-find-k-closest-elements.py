class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        
        for num in arr:
            heappush(heap, (abs(num - x), num))
        
        ans = []
        for _ in range(k):
            ans.append(heappop(heap)[1])
            
        ans.sort()
        return ans