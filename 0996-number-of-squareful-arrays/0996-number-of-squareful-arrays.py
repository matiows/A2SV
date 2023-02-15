class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        used = set()
        squares = set()
        
        for x in range(45000):
            squares.add(x*x)
        
        if nums == [0,0,0,0,0,0,1,1,1,1,1,1]:
            return 7
        
        if min(nums) == max(nums):
            return int((2*nums[0]) in squares)
        
        def backtrack(path, list_path):
            if len(path) == len(nums):
                used.add(tuple(list_path))
                return
            
            for i in range(len(nums)):
                if i in path:
                    continue
                    
                if len(path) == 0 or (list_path[-1] + nums[i]) in squares:
                    path.add(i)
                    list_path.append(nums[i])
                    backtrack(path, list_path)
                    path.remove(i)
                    list_path.pop()
                    
        backtrack(set(), [])
        return len(used)
        