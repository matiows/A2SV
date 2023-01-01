class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_map = {}
        sentence = s.split(" ")
        matched = set()
        i = 0
        
        if len(pattern) != len(sentence):
            return False
        
        while i < len(pattern):
            ch = pattern[i]
            word = sentence[i]
            
            if ch in hash_map:
                if hash_map[ch] != word:
                    return False
            else:
                if word in matched:
                    return False
                
                hash_map[ch] = word
                matched.add(word)
            
            i += 1
        
        return True
            
        