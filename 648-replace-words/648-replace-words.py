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
    
    def search(self, word):
        current = self.root
        result = ""
        for char in word:
            if current.isWord:
                return result
            if char not in current.children:
                return False
            current = current.children[char]
            result += char
    
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        result = []
        for word in dictionary:
            self.insert(word)
            
        sentence = (sentence.split(' '))
        for word in sentence:
            check = self.search(word)
            if check:
                result.append(check)
            else:
                result.append(word)
        return ' '.join(result)
            
            