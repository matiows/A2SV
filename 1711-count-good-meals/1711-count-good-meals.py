class Solution:
    def add(self, a, b):
        res = a + b
        if res >= self.MOD:
            res -= self.MOD
        return res
    
    
    def countPairs(self, deliciousness: List[int]) -> int:
        count = defaultdict(int)
        length = len(deliciousness)
        ans = 0
        self.MOD = 1_000_000_007
        
        for i in range(length):
            for s in range(22):
                pow_2 = (1 << s)
                dif = pow_2 - deliciousness[i]
                
                if dif in count:
                    ans = self.add(ans, count[dif])
                
            count[deliciousness[i]] += 1
        
        return ans
                
                
        