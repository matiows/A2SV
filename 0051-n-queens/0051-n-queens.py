class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:        
        answer = []
        current = [['.']* n for _ in range(n)]
        col_visited = set()
        diag_visited = set()
        inv_diag_visited = set()
        
        def checkCell(row, col):
            if row + col in diag_visited:
                return False
            if row - col in inv_diag_visited:
                return False
            if col in col_visited:
                return False
            
            return True
        
        def putQueen(row):
            if row == n:
                temp = []
                for r in current:
                    temp.append(''.join(r))
                    
                answer.append(temp)
                return
            
            for new_col in range(n):
                if checkCell(row, new_col):
                    current[row][new_col] = 'Q'
                    col_visited.add(new_col)
                    diag_visited.add(row + new_col)
                    inv_diag_visited.add(row - new_col)
                    
                    putQueen(row + 1)
                    
                    current[row][new_col] = '.'
                    col_visited.remove(new_col)
                    diag_visited.remove(row + new_col)
                    inv_diag_visited.remove(row - new_col)
                      
        putQueen(0)
        return answer
                
        