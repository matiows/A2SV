class Solution:
    def reverseString(self, s: List[str]) -> List[str]:
        s = self.reverse(0,len(s)-1,s)
    
    def reverse(self, l , r, s: List[str]):
        if l >= r:
            return
        s[l], s[r] = s[r],s[l]
        self.reverse(l+1, r-1, s)