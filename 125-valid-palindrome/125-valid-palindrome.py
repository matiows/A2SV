class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s:
            if not i.isalnum():
                s= s.replace(i, "")
        start = 0
        end = len(s)-1

        while(start!=end):
            if end<0:
                return True
            if s[start].lower() == s[end].lower():
                start = start+1
                end = end -1
            else:
                return False
        return True