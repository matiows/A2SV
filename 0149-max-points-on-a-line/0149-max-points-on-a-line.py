class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        answer = 1
        
        for i, (x1, y1) in enumerate(points):
            line = defaultdict(int)
            for j in range(len(points)):
                if i == j:
                    continue
                x2, y2 = points[j]
                m = (y2 - y1) / (x2 - x1) if x1 != x2 else inf
                
                line[m] += 1
                answer = max(answer, line[m] + 1)
        return answer
                