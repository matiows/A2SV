class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        n = len(grid)
        queue = deque()
        queue.append((0,0))
        steps = 1
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        inbound = lambda r, c:  0 <= r < n and 0 <= c < n
        
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if (row, col) == (n-1, n-1):
                        return steps
                
                for x, y in directions:
                    new_r, new_c = row + x, col + y
                    
                    if inbound(new_r, new_c) and grid[new_r][new_c] == 0:
                        grid[new_r][new_c] = 1
                        queue.append((new_r, new_c))
                        
            steps += 1
            
        return -1
            