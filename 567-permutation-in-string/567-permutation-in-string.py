class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = [0] * 26
        check = [0] * 26
        n1 = len(s1)
        n2 = len(s2)
        
        if n2 < n1:
            return False
        
        for ch in s1:
            count[ord(ch) - ord('a')] += 1
        
        for i in range(n1):
            check[ord(s2[i]) - ord('a')] += 1
           
        if check == count:
            return True
        
        left = 0
        for i in range(n1, n2):
            check[ord(s2[left]) - ord('a')] -= 1
            left += 1
            
            check[ord(s2[i]) - ord('a')] += 1
        
            if check == count:
                return True
        
        return False