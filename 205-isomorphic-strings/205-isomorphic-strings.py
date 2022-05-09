from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        check_s = defaultdict(int)
        check_t = defaultdict(int)
        result = True
        for i in range(len(s)):
            if check_s[s[i]] == 0 and check_t[t[i]] == 0:
                check_s[s[i]] = t[i]
                check_t[t[i]] = s[i]
            elif check_s[s[i]] != t[i] and check_t[t[i]] != s[i]:
                result = False
        return result