class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) + 1)
        answer = []
        
        for start, end, direction in shifts:
            if direction == 1:
                prefix[start] += 1
                prefix[end + 1] -= 1
            else:
                prefix[start] -= 1
                prefix[end + 1] += 1
            
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]
            
        for idx, char in enumerate(s):
            new_ord = ord(char) - ord('a') + prefix[idx]
            new_ord %= 26
            new_ord += ord('a')
            answer.append(chr(new_ord))
   
        return ''.join(answer)