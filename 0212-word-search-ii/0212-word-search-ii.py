class TrieNode:
    def __init__(self, val: str = None, parent: Optional['TrieNode'] = None):
        self.children = {}
        self.val = val
        self.parent = parent
        self.word = None
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(val=c, parent=node)
            node = node.children[c]
        node.word = word    
    
    def prune(self, node: TrieNode) -> None:
        node.word = None

        child = node
        parent = child.parent
        while parent and len(child.children) == 0:
            del parent.children[child.val]
            child = parent
            parent = parent.parent

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        m, n = len(board), len(board[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        inbound = lambda x, y : 0 <= x < m and 0 <= y < n
        answer = set()

        def backtrack(row, col, node):
            char = board[row][col]
            
            if char not in node.children:
                return
        
            node = node.children[char]
            board[row][col] = '#'
                
            if node.word:
                answer.add(node.word)
                trie.prune(node)
                
            for x, y in directions:
                new_row = row + x
                new_col = col + y
                if inbound(new_row, new_col) and board[new_row][new_col] != '#':
                    backtrack(new_row, new_col, node)
                    
            board[row][col] = char

        for row in range(m):
            for col in range(n):
                
                backtrack(row, col, trie.root)

        return list(answer)