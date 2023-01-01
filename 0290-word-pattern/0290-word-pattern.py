class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_map = {}
        sentence = s.split(" ")
        i = 0
        
        if len(pattern) != len(sentence):
            return False
        
        if len(set(pattern)) != len(set(sentence)):
            return False
        
        while i < len(pattern):
            ch = pattern[i]
            word = sentence[i]
            
            if ch not in hash_map:
                hash_map[ch] = word
                
            elif hash_map[ch] != word:
                return False
                            
            i += 1
        
        return True
            
        