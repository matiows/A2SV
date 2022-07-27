class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            temp = (r - l) * min(height[l], height[r])
            area = max(temp, area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area