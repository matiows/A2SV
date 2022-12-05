class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maximum = [0]
        
        def helper(start,array,s):
            if len(s)==len(set(s)):
                maximum[0] = max(maximum[0], len(s))
            
            else:
                return
            
            for i in range(start,len(array)):
                helper(i+1,array,s + array[i])
        
        helper(0,arr,"")
        return maximum[0]