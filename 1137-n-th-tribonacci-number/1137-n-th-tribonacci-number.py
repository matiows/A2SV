class Solution:
    @lru_cache(None)
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n <= 2:
            return 1
        
        third = self.tribonacci(n - 3)
        second = self.tribonacci(n - 2)
        first = self.tribonacci(n - 1)
        
        return first + second + third
        