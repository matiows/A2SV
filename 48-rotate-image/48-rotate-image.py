class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead
        """
        n = len(matrix)
        temp = [row[:] for row in matrix]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = temp[n-j-1][i]