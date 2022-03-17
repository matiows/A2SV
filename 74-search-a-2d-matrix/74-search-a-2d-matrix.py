class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def toMatrix (indx):
            n = indx % len(matrix[0])
            m = indx // len(matrix[0])
            return [m, n]
        
        left = 0
        right = len(matrix) * len(matrix[0])
        right -= 1
            
        while left <= right:
            mid = (left + right) // 2
            _mid = toMatrix(mid)
            
            if matrix[_mid[0]] [_mid[1]] == target:
                return True
            
            elif matrix[_mid[0]] [_mid[1]] < target:
                left = mid + 1
                
            else:
                right = mid - 1
                
        return False
        