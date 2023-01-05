class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        slope = defaultdict(set)
        vertical = defaultdict(set)
        answer = 1
        
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[i+1:]:
                if x1 == x2:
                    vertical[x1].add(y1)
                    vertical[x1].add(y2)
                    answer = max(answer, len(vertical[x1]))
                else:
                    m = (y2 - y1)/(x2 - x1)
                    b = y2 - m*x2
                    slope[(m,b)].add((x2, y2))
                    slope[(m,b)].add((x1, y1))
                    answer = max(answer, len(slope[(m,b)]))
                    
        return answer