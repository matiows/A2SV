class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        di = defaultdict(int)
        _max = 0
        length = 0
        left = 0
        right = 0
        
        while right < len(s):
            di[s[right]] += 1
            _max = max(_max, di[s[right]])
            
            if ((right-left+1) - _max) > k:
                di[s[left]] -= 1
                left += 1
                
            else:
                length = max(_max, right-left+1)
                
            right += 1
            
        return length