class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        length = len(palindrome)
        if length == 1:
            return ""
        
        result = ""
        for idx in range(length//2):
            if palindrome[idx] != 'a':
                result = palindrome[:idx] + 'a' + palindrome[idx + 1:]
                return result
       
        result = palindrome[:-1] + 'b'
        return result
        