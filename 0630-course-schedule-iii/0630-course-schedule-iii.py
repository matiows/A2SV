class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []
        courses.sort(key = lambda x: (x[1], x[0]))
        time = 0
        
        for duration, last in courses:
            if duration > last:
                continue
                
            time += duration
            heappush(heap, duration * -1)
            
            while time > last and heap:
                value = heappop(heap)
                time += value
            
            
        return len(heap)