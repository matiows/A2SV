class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def sortFun(point):
            return(point[0]**2+point[1]**2)
        points.sort(key=sortFun)
        return points [:k]