class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        check = bin(n)
        return check.count('1') == 1 and n > 0