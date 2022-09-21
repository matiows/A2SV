from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for string in strs:
            temp = [0]*26
            for ch in string:
                temp[ord(ch) - 97] += 1
                
            anagram[tuple(temp)].append(string)
        result = list(anagram.values())
        return result
            
        