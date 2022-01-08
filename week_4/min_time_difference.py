class Solution:
    def sort_by_difference(self, points):
        if points[1]-points[0]>(12*60):
            result = (points[0]+1440)-points[1]
        else:
            result = points[1]-points[0]
        return result
        
    def findMinDifference(self, timePoints: List[str]) -> int:
        points = []
        for point in timePoints:
            x,y = map(int, point.split(":"))
            x*=60
            points.append(x+y)
        points.sort()
        pairPoints = [(i,j) for i,j in zip(points, points[1:])]
        pairPoints.append((points[0],points[len(points)-1]))
        pairPoints.sort(key = self.sort_by_difference)
        return self.sort_by_difference(pairPoints[0])