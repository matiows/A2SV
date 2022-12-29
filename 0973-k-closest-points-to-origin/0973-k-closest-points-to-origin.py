import numpy as np
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        close_points = []
        for i in range(0, len(points)):
            a = (points[i][0], points[i][1])
            b = (0, 0)
            distance=dist(a,b)
            temp = [points[i][0], points[i][1], distance]
            close_points.append(temp)
        close_points.sort(key = lambda x: x[2])
        close_points = np.array(close_points)
        return close_points [:k, 0:2]
