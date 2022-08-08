class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = list(t)
        s = list(s)
        t.sort()
        s.sort()
        return t == s
        