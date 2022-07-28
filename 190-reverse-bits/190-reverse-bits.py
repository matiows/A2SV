class Solution:
    def reverseBits(self, n: int) -> int:
        string = bin(n)[2:]
        string = string[::-1] + '0' * (32 - len(string))
        return int(string, 2)
        