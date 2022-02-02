class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 1000000007
        rem = n % 2
        n -= rem
        result = pow (20, n//2, mod)
        
        if rem == 1:
            result *= 5
            
        
        return result % mod
        