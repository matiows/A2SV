class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = self.findInverse(n)
        return s[k-1]
       
    def findInverse(self, n: int) -> str:

        if n == 1:
            return '0'
        
        s = self.findInverse(n-1)

        inverse = str()

        for i in range(len(s)-1,-1,-1):
            
            if s[i] == '0':
                inverse+='1'
            
            else:
                inverse+='0'
        
        s = s + '1' + inverse
        
        return s