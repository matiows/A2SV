class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = blocks[:k].count('W')
        answer = count
        left = 0
        
        for i in range(k, len(blocks)):
            count += int(blocks[i] == 'W')
            count -= int(blocks[left] == 'W')
            left += 1
            answer = min(answer, count)
            
        return answer