class Solution:
    def binRight(self, stack, target):
        left = len(stack)
        right = 0
        
        while right + 1 < left:
            mid = (left + right) // 2
            if target <= stack[mid]:
                right = mid

            else:
                left = mid
        
        # print(stack, target, len(stack) - right)
        return len(stack) - right
            
            
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        stack = [heights[-1]]
        answer = [0] * len(heights)
        
        for i in range(len(heights) - 2, -1, -1):
            count = self.binRight(stack, heights[i])
            answer[i] = count
            
            while stack and stack[-1] < heights[i]:
                stack.pop()
                
            stack.append(heights[i])
        
        return answer
        
        