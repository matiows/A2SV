class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = set()
        original = image[sr][sc]
        m, n = len(image), len(image[0])
        
        def dfs(row, col):
            visited.add((row,col))
            image[row][col] = newColor
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            for x, y in directions:
                new_row, new_col = row + x, col + y
                
                if 0 <= new_row < m and 0 <= new_col < n and image[new_row][new_col] == original and (new_row, new_col) not in visited:
                    dfs(new_row, new_col)
        
        dfs(sr, sc)
        
        return image