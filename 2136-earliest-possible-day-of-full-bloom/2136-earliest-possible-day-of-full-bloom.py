class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        num_plants = len(plantTime)
        key = lambda a: (a[0], -a[1])
        time = list(zip(growTime, plantTime))
        
        time.sort(key = key, reverse = True)
        early_time = 0
        cur_time = 0
        
        for grow_time, plant_time in time:
            cur_time += plant_time
            early_time = max(early_time, cur_time + grow_time)
        
        return early_time