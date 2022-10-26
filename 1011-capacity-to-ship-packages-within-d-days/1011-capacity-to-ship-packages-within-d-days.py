class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        length = len(weights)
        sum_weights = sum(weights)
        
        def findWeight(mid):
            running_sum = 0
            count = 1
            for weight in weights:
                if running_sum + weight <= mid:
                    running_sum += weight
                elif weight <= mid:
                    count += 1
                    running_sum = weight
                else:
                    return float('inf')
            return count
        
        minimum = min(weights)
        maximum = sum_weights
        answer = maximum
        
        while minimum <= maximum:
            mid = (minimum + maximum) // 2
            count = findWeight(mid)

            if count <= days:
                answer = min(mid, answer)
                maximum = mid - 1

            elif count > days:
                minimum = mid + 1
            
        return answer