class AllOne:

    def __init__(self):
        self.wordNum = defaultdict(int)
        self.numWord = defaultdict(set)

    def inc(self, key: str) -> None:
        count = self.wordNum[key]
        if key in self.numWord[count]:
            self.numWord[count].remove(key)
            
        self.wordNum[key] += 1
        self.numWord[count + 1].add(key)
        
        if len(self.numWord[count]) == 0:
            self.numWord.pop(count)

    def dec(self, key: str) -> None:
        count = self.wordNum[key]
        if key in self.numWord[count]:
            self.numWord[count].remove(key)
        
        self.wordNum[key] -= 1
        
        if count > 1:
            self.numWord[count - 1].add(key)
        
        if len(self.numWord[count]) == 0:
            self.numWord.pop(count)

    def getMaxKey(self) -> str:
        if self.numWord:
            count = max(self.numWord.keys())
            for element in self.numWord[count]:
                return element
        else:
            return ""

    def getMinKey(self) -> str:
        if self.numWord:
            count = min(self.numWord.keys())
            for element in self.numWord[count]:
                return element
        else:
            return ""
        
        
        '''
        a:0
        b:0
        c:3
        '''


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()