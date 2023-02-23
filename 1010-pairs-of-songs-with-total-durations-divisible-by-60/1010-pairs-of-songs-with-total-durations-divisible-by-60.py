class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        arr2 = [i%60 for i in time]
        count_dict = Counter(arr2)
        count = 0
        
        for i in range(1, 30):
            count += count_dict[i] * count_dict[60-i]
                        
        count += count_dict[30] * (count_dict[30]-1)  // 2
        count += count_dict[0] * (count_dict[0] -1)  // 2
            
        return count