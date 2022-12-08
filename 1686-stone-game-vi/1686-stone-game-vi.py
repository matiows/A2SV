class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        heap = []
        
        for i in range(len(aliceValues)):
            heapq.heappush(heap, (-1*aliceValues[i] + (-1*bobValues[i]), i))
            # heapq.heappush(heap, (-1*bobValues[i], -1*aliceValues[i], i))

        # print(aliceValues)
        # print(bobValues)
        length = 0
        flag = 0
        visited = set()
        score = 0
            
        while length < len(aliceValues):
            temp = heappop(heap)
            while temp[1] in visited:
                temp = heappop(heap)
            
            if flag == 0:
                score += aliceValues[temp[1]]
            
            else:
                score -= bobValues[temp[1]]
                
            visited.add(temp[1])

            flag = 1-flag
        
            length += 1
            
        if score > 0:
            return 1
        elif score < 0:
            return -1
        else:
            return 0 