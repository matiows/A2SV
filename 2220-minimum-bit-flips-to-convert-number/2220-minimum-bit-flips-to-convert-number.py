class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s = bin(start)[2:]
        g = bin(goal)[2:]
        count = 0
        
        if len(s) > len(g):
            g = '0'*(len(s) - len(g)) + g
        elif len(g) > len(s):
            s = '0'*(len(g) - len(s)) + s
        
        for i in range(len(g)):
            count += int(s[i]) ^ int(g[i])
                
        return count