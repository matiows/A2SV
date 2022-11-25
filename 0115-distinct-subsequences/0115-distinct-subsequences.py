class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def match(ss, tt):
            if (ss, tt) in memo:
                return memo[(ss, tt)]
            if tt == t_length:
                return 1
            if s_length - ss < t_length - tt or ss == s_length:
                return 0
            result = 0
            if t[tt] == s[ss]:
                result = match(ss + 1, tt + 1)
            result += match(ss + 1, tt)
            memo[(ss, tt)] = result
            return result
        t_length = len(t)
        s_length = len(s)
        s = list(s)
        t = list(t)
        return match(0, 0)