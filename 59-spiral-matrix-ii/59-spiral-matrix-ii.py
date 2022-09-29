class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for i in range(n)] for j in range(n)]
        x = 1
        r,c = 0,0
        
        while x <= n*n:
            i,j = r,c
            
            for l in range(j, n - c):
                ans[i][l] = x
                j += 1
                x += 1
            j -= 1
            i += 1
            
            for k in range(i, n - r):
                ans[k][j] = x
                i += 1
                x += 1
            i -= 1
            j -= 1
            
            for o in range(j, c - 1 ,-1):
                ans[i][o] = x
                j-=1
                x+=1
            j += 1
            i -= 1
            
            for p in range(i, r ,-1):
                ans[p][j] = x
                x+=1
            r+=1
            c+=1
        return ans