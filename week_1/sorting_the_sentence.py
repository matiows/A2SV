class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        temp = ['']*len(words)        
        for i in range (0, len(words)):
            word = words[i]
            index = int(word[len(word)-1])-1
            temp[index] = word[:-1]
        structured = " ".join(temp)
        return structured