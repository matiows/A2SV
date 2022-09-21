class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        p_count = [0]*26
        s_count = [0]*26
        for i in range(len(p)):
            p_count[ord(p[i])-97] += 1
            s_count[ord(s[i])-97] += 1
            
        result = [0] if p_count == s_count else []
        l = 0
        
        for r in range(len(p), len(s)):
            s_count[ord(s[r])-97] += 1
            s_count[ord(s[l])-97] -= 1
            
            l+=1
            if p_count == s_count:
                result.append(l)
        return result