class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        road = [0] * 1001
        
        for passenger, start, end in trips:
            road[start] += passenger
            road[end] -= passenger
          
        for i in range(len(road)-1):
            road[i+1] = road[i+1] + road[i]
            if road[i] > capacity:
                return False

        return True