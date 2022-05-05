class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo=defaultdict(int)
        result = []
        
        def findPower(num):
            if num == 1:
                return 0
            
            if memo[num] != 0:
                return memo[num]
            
            steps = 0
            if num%2 == 0:
                temp = num//2
                step = findPower(temp) + 1
                memo[num] = step
                return step
            
            else:
                temp = (num * 3) + 1 
                step = findPower(temp) + 1
                memo[num] = step
                return step
            
        for num in range(lo, hi+1):
        
            result.append((findPower(num), num))
        
        result.sort()
        return result[k-1][1]