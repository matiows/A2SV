class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = defaultdict(int)
        check = defaultdict(int)
        len_t = len(t)
        len_s = len(s)
        ans = [-1,float('inf')]
        
        if len_t > len_s:
            return ""
        
        def match():
            for key, value in count.items():
                if check[key] < value:
                    return False
            return True
        
        for i in range(len_t):
            count[t[i]] += 1
            check[s[i]] += 1
          
        if match():
            return s[:len_t]
        
        l = 0
        r = len_t
        
        while r < len_s:
            if not match():
                check[s[r]] += 1
                r += 1
                
            while match():
                if r-l < ans[1] - ans[0]:
                    ans = [l,r]
                check[s[l]] -= 1
                l += 1
        
        if ans[0] >= 0:
            return s[ans[0]:ans[1]] 
        return ""            