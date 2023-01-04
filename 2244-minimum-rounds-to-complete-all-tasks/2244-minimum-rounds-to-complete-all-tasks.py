from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        answer = 0
        
        for key, value in count.items():
            if value == 1:
                return -1
            
            answer += (value + 2)//3
                
        return answer