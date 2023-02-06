class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x: len(x))
        count = {}
        answer = 1
        for word in words:
            count[word] = 1
            
        for word in words:
            if len(word) > 1:
				
                for i in range(len(word)):
                    temp = word[:i] + word[i+1:]
                    
                    if temp in count:
                        count[word] = max(count[word], 1 + count[temp])
                        answer = max(answer, count[word])
        
        return answer