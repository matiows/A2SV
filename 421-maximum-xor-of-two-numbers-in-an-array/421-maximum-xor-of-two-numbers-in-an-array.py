class TrieNode:
    def __init__(self):
        self.node = [None, None]
        self.num = 0
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
           
    def insert(self, num):
        current = self.root
        for b in range(31, -1, -1):
            _bit = bool(num & (1 << b))
            if not current.node[_bit]:
                current.node[_bit] = TrieNode()
            current = current.node[_bit]
        current.num = num
        
    def searchMax(self, num):
        current = self.root
        for b in range(31, -1, -1):
            _bit = bool(num & (1 << b))
            if current.node[not _bit]:
                current = current.node[not _bit]
            else:
                current = current.node[_bit]
        return current.num
        
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            self.insert(num)
        for num in nums:
            ans = max(ans, num ^ self.searchMax(num))
        return ans