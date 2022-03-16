class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        
        for i in range(len(grid)):
            left = 0
            right = len(grid[0]) - 1
            temp = len(grid[0])

            while left <= right:
                mid =  left + (right -  left) // 2
                
                if grid[i][mid] < 0:
                    temp = mid
                    right = mid - 1
                else:
                    left = mid + 1
            result += (len(grid[0]) - temp)
        
        return result
                
        