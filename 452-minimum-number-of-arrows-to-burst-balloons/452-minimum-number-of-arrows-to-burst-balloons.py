class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        prevEnd = points[0][1]
        
        result = 1
        
        for start, end in points[1:]:
            
            if prevEnd >= start:
                prevEnd = min(prevEnd, end)
                
            else:
                result += 1
                prevEnd = end
                
        return result