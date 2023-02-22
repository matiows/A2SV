class Solution:
    def secondsToRemoveOccurrences(self, s):
        check = '01'
        count = 0
        
        if check not in s: 
            return 0
        
        while check in s:
            s = s.replace(check, '10')
            count += 1

        return count