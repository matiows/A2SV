class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        small = len(str2)
        long = len(str1)
        if long < small:
            str1, str2 = str2, str1
            long, small = small, long
        
        answer = ""
        
        for idx in range(1, small+1):
            if str1.count(str2[:idx]) == (long/idx) and str2.count(str2[:idx]) == (small/idx):
                answer = str2[:idx]
                
        return answer