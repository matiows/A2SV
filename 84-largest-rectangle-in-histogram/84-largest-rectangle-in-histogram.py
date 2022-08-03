class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
#   create an increasing monotonic stack 
#   whenever we get a decreasing height check the max area and pop it

        stack = []
        maxArea = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max((height * (i - index)), maxArea)
                start = index
            stack.append((start, h))
        
        for i,h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)
        
        return maxArea