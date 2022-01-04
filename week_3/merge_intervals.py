class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        new=[intervals[0]]
        j = 0
        for i in range(1, len(intervals)):
            if new[j][1]>=intervals[i][0] and new[j][1] < intervals[i][1]:
                new[j][1] = intervals[i][1]
            elif new[j][1]<intervals[i][0]:
                new.append(intervals[i])
                j+=1
        return new