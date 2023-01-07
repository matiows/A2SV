class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        i = 0
        while i < len(costs) and costs[i] <= coins:
            coins -= costs[i]
            count += 1
            i += 1

        return i