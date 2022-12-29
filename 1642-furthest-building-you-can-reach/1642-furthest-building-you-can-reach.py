class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        total = 0
        i = 1
        heap = []
        while total <= bricks and i < len(heights):
            if heights[i] > heights[i-1]:
                diff = heights[i] - heights[i-1]
                heappush(heap, diff * -1)
                total += diff
                
            if total > bricks:
                if ladders:
                    height = heappop(heap)
                    height *= -1
                    total -= height
                    ladders -= 1
                else:
                    break
                
            i += 1
            
        return i - 1
                