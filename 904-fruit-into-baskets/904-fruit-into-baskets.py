from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        ids = defaultdict(lambda : -1)
        basket1 = basket2 = max_count = 0
        
        for i in range(len(fruits)):
            if basket1 == 0 or ids['basket1'] == fruits[i]:
                basket1 += 1    
                ids['basket1'] = fruits[i]
            
            elif basket2 == 0 or ids['basket2'] == fruits[i]:
                basket2 += 1
                ids['basket2'] = fruits[i]
            
            else:
                max_count = max(max_count, basket1+basket2)
                temp = fruits[i-1]
                count = 0
                
                for j in range(i-1,-1,-1):
                    if fruits[j] != temp:
                        break
                    count += 1
                
                if ids['basket1'] == temp:
                    ids['basket2'] = fruits[i]
                    basket2 = 1
                    basket1 = count
                
                else:
                    ids['basket1'] = fruits[i]
                    basket1 = 1
                    basket2 = count
                    
        return max(max_count, basket1+basket2)