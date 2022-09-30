class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        windows = []
        
        for i in range(len(s)//2, 0, -1):
            if len(s) % i == 0:
                windows.append(i)
            
        for j in windows:
            i = 0
            check = s[i:j]
            check = check * (len(s) // j)
            
            if check == s:
                return True
            
        return False