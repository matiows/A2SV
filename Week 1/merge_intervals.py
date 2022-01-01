class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new = []
        for j in range(len(intervals)):
            for i in range(1,len(intervals)):
                if intervals[i-1][1]>=intervals[i][0]:
                    intervals[i-1][1]=intervals[i][1]
                    intervals.pop(i)
                    break
                elif intervals[i-1][1]>=intervals[i][0]:
                    intervals[i-1][1]=intervals[i][1]
                    intervals.pop(i)
                    break
        return intervals