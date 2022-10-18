class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel_prefix = [0]
        for cost in travel:
            travel_prefix.append(travel_prefix[-1] + cost)
        
        glass = 0
        metal = 0
        paper = 0
        count = 0
        for idx, house in enumerate(garbage):
            G = house.count('G')
            P = house.count('P')
            M = house.count('M')
            count += len(house)
            if G:
                glass = idx
            if M:
                metal = idx
            if P:
                paper = idx
        
        answer = count + travel_prefix[paper] + travel_prefix[glass] + travel_prefix[metal]
        
        return answer
            