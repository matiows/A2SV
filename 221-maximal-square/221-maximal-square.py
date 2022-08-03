class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        i = 0
        j = 0
        maxArea = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    continue
                area = int(matrix[i][j])
                r = i + 1
                c = j + 1
                
                while r < len(matrix) and c < len(matrix[0]):
                    columnSum = sum([int(row[c]) for row in matrix[i:r]])
                    rowSum = sum(map(int, matrix[r][j:c+1]))
                    if columnSum != (r-i) or rowSum != (c - j + 1):
                        break
                    area += columnSum
                    area += rowSum
                    
                    r += 1
                    c += 1
                if r == len(matrix) and area > maxArea:
                    return area                    
                maxArea = max(area, maxArea)
        return maxArea   