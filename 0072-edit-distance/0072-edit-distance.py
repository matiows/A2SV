class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        memo = {}
        
        def topDown(index1, index2):
            if index1 == len(text1):
                return len(text2) - index2
            
            if index2 == len(text2):
                return len(text1) - index1
            
            if (index1, index2) in memo:
                return memo[(index1, index2)]
            
            check = int(text1[index1] == text2[index2])
            delete = replace = insert = move = float('inf')
    
            if not check:
                insert = topDown(index1, index2 + 1) + 1
                delete = topDown(index1 + 1, index2) + 1
                replace = topDown(index1 + 1, index2 + 1) + 1
                result = min(delete, insert, replace)
                memo[(index1, index2)] = result
                return result
            
            else:
                move = topDown(index1 + 1, index2 + 1)
                memo[(index1, index2)] = move
                return move        
            
        answer = topDown(0, 0)
        return answer