class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = 0
        for ban in piles:
            total += ban
            
        _min = ceil(total / h)
        _max = max(piles)
        
        ans = _max + 1
        
        while _min <= _max:
            mid = _min + (_max - _min) // 2
            # print(_min, mid, _max)
            temp = 0
            for ban in piles:
                temp += ceil(ban / mid)
            
            if temp == h:
                ans = min(ans, mid)
                _max = mid - 1
            elif temp < h:
                _max = mid - 1
            else:
                _min = mid + 1
            # print(temp)
        
        return ans if ans <= _max else _min 
            
                