class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        way = 0
        num = 1
        row = 0
        col = 0
        
        while num <= n*n:
            matrix[row][col] = num
            num += 1
            
            r = (row + directions[way][0]) % n
            c = (col + directions[way][1]) % n
            
            if matrix[r][c] != 0:
                way = (way + 1) % 4
                
            row += directions[way][0]
            col += directions[way][1]
            
        return matrix