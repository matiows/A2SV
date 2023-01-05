class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        new = [points[0]]
        j = 0
        # print(points)
        for i in range(1, len(points)):
            if new[j][1] >= points[i][0]:
                new[j][1] = min(new[j][1], points[i][1])
            else:
                new.append(points[i])
                j += 1
        # print(new)
        return len(new)