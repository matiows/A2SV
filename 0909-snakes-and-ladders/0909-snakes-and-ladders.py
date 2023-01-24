class Solution:
    def findCordinate(self, num, size):
        row = size - 1 - ((num - 1) // size)
        col = (num - 1) % size
        if (size - row) % 2 == 0:
            col = size - 1 - col
        
        return row, col
        
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        queue = deque()
        queue.append(1)
        count = 0
        size = len(board)
        win = size * size
        
        while queue:
            for _ in range(len(queue)):
                val = queue.popleft()
                if val == win:
                    return count
                
                maximum = 0
                for cur in range(val + 1, min(val + 7, win + 1)):
                    row, col = self.findCordinate(cur, size)
                    if board[row][col] == -1:
                        maximum = max(maximum, cur)
                    elif board[row][col] > 0:
                        queue.append(board[row][col])
                        board[row][col] = 0
                        
                if maximum:
                    queue.append(maximum)
            
            count += 1
            
        return -1
            