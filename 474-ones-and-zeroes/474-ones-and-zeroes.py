class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = [0]*len(strs)
        for i,s in enumerate(strs):
            zeros = s.count('0')
            counts[i] = (zeros, len(s)-zeros)
        memo = {}
        
        def dp(i, zeros, ones):
            if (i, zeros, ones) in memo:
                return memo[(i, zeros, ones)]
            
            if zeros < 0 or ones < 0:
                return float('-inf')
            
            if i >= len(strs):
                return 0
            
            if zeros == 0 and ones == 0:
                return 0
      
            z_cnt , o_cnt = counts[i][0], counts[i][1]

            re = max((dp(i + 1, zeros - z_cnt, ones - o_cnt) + 1),
                       dp(i + 1, zeros, ones))
            memo[(i, zeros, ones)] = re
            return re
        return dp(0, m, n)
            