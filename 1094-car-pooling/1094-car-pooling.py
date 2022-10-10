class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ride = [0] * 1001
        
        for no, st, en in trips:
            if no > capacity:
                return False
            
            ride[st] += no
            ride[en] -= no
            
        for i in range(len(ride)):
            capacity -= ride[i]
            if capacity < 0:
                return False
        
        return True