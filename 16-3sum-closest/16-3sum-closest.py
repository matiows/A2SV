class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
                
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                check = nums[i] + nums[l] + nums[r]
                if abs(check - target) < abs(closest - target):
                    closest = check
                
                if check == target:
                    return check
                elif check < target:
                    l += 1
                else:
                    r -= 1
                
        return closest