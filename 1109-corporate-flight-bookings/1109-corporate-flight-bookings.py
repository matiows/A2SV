class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        bookings.sort()
        ride = [0]*(n+1)
        
        for st, en, seat in bookings:
            ride[st-1] += seat
            ride[en] -= seat
            
        for i in range(1, n):
            ride[i] += ride[i-1]
            
        return ride[:n]
        