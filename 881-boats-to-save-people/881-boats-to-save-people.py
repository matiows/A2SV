class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        pt1 = 0
        pt2 = len(people) - 1
        
        counter = 0
        
        while pt1 <= pt2:
            
            if people[pt1] + people[pt2] <= limit:
                pt1 += 1
                pt2 -= 1
            
            else:
                pt2 -= 1
            
            counter += 1
        
        return counter