class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        
        def topDown(index1, index2):
            if index1 > len(text1) - 1 or index2 > len(text2) - 1:
                return 0
            
            check = int(text1[index1] == text2[index2])
            
            if index1 == len(text1) - 1 and index2 == len(text2) - 1:
                return check
            
            if (index1, index2) in memo:
                return memo[(index1, index2)]
            
            result = 0
            if check:
                result = topDown(index1 + 1, index2 + 1) + 1
                memo[(index1, index2)] = result
                return result
            
            else:
                if index1 < len(text1) - 1:
                    result = max(result, topDown(index1 + 1, index2))
                
                if index2 < len(text2) - 1:
                    result = max(result, topDown(index1, index2 + 1))
                    
            memo[(index1, index2)] = result
            return result
        
        answer = topDown(0,0)
            
        return answer