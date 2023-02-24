class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        minutes = defaultdict(set)
        
        for uid, minute in logs:
            minutes [uid].add(minute)
            
        ans = [0 for _ in range(k)]
        
        for key in minutes :
            ans[len(minutes[key]) - 1] += 1
        
        return ans