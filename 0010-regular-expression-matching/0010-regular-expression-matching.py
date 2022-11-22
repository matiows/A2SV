class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        @lru_cache(None)
        def regExp(ss, pp):
            if ss >= len(s) and pp >= len(p):
                return True
            
            if pp >= len(p):
                return False
            
            match = (ss < len(s) and (s[ss] == p[pp] or p[pp] == '.'))
            if pp + 1 < len(p) and p[pp + 1] == '*':
                return regExp(ss, pp+2) or (match and regExp(ss+1, pp))
            
            
            if match:
                return regExp(ss+1, pp+1)
            
            return False
        
        return regExp(0, 0)