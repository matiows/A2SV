class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        _len = len(flowerbed)
               
        if _len <= 2 and max(flowerbed) == 0:
            n -= 1
        
        else:
            l, m, r = 0, 1, 2
            while r < _len:
                
                if max(flowerbed[l], flowerbed[m]) == 0 and l == 0:
                    flowerbed[l] = 1
                    n -= 1
                    
                elif max(flowerbed[l], flowerbed[m], flowerbed[r]) == 0:
                    flowerbed[m] = 1
                    n -= 1
                    
                if max(flowerbed[m], flowerbed[r]) == 0 and r+1 == _len:
                    n -= 1
                    break
                    
                l = m
                m = r
                r += 1 

        return n <= 0
            