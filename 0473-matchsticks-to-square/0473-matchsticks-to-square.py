class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4
        length = len(matchsticks)
        used = [False] * length
        
        def backtrack(index, count, stick_sum):
            if count == 0:
                return True
            
            if stick_sum == target:
                return backtrack(0, count - 1, 0)
            
            for i in range(index + 1, length):
                if not used[i] and stick_sum + matchsticks[i] <= target:
                    used[i] = True
                    
                    if backtrack(i, count, stick_sum + matchsticks[i]):
                        return True
                    
                    used[i] = False
                    
            return False
        
        used[0] = True
        return backtrack(0, 4, matchsticks[0])
        