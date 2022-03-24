class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        alph = {}

        for i in range(len(s)):
            if s[i] not in alph.keys():
                alph[s[i]] = [i, i]
            else:
                alph[s[i]][1] = i

        intervals = []
        result = []
        
        intervals = [x for x in alph.values()]

        intervals.sort()
        
        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(intervals[i][1], end)
            else:
                result.append(end - start + 1)
                start, end = intervals[i][0], intervals[i][1]
        result.append(end - start + 1)

        return result