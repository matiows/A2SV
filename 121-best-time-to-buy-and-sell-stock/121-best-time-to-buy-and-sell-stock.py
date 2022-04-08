class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 1:
            return 0
        
        minimum = prices[0]
        maximum = 0
        
        for i in range(1, len(prices)):
            minimum = min(minimum, prices[i])
            maximum = max(maximum, prices[i] - minimum)
            
        return maximum