class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
           
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.isWord = True
        
    def longestWord(self, words: List[str]) -> str:
        result = ''
        
        for word in words:
            self.insert(word)
            
        for word in words:
            current = self.root
            for char in word:
                current = current.children[char]
                if not current.isWord:
                    break
            if current.isWord: 
                if (len(word) > len(result)) or (len(word) == len(result) and word < result):
                    result = word
        return result
                