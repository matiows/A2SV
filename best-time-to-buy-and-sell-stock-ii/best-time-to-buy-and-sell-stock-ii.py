class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l+1
        _sum = 0
        if len(prices) == 1:
            return 0
        
        while r < len(prices):
            if prices[r] < prices[r-1]:
                _sum += prices[r-1] - prices[l]
                l = r
                r = l+1
                
            elif prices[r] > prices[l] and r == len(prices)-1:
                _sum += prices[r] - prices[l]
                r += 1
            else:
                r += 1
        return _sum
                
                
            
        