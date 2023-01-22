class Solution:
    @lru_cache(None)
    def isPalindrome(self, s, l, r):
        result = True
        while l < r:
            if s[l] != s[r]:
                result = False
                break
            l += 1
            r -= 1

        return result
    
    def backtrack(self, s, cut, palindromes):
        if cut == len(s):
            return [palindromes]
        
        result = []
        for idx in range(cut, len(s)):
            if self.isPalindrome(s, cut, idx):
                palindromes.append(s[cut:idx+1])
                temp = self.backtrack(s, idx + 1, palindromes.copy())
                result.extend(temp.copy())
                palindromes.pop()
        return result
    
    def partition(self, s: str) -> List[List[str]]:
        result = self.backtrack(s, 0, [])
        
        return result    