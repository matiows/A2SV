class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = []
        stack.append(-1)
        maxLength = 0
        for idx, char in enumerate(s):
            if char == "(":
                stack.append(idx)
            else:
                stack.pop()
                if not stack:
                    stack.append(idx)
                else:
                    maxLength = max(maxLength, idx - stack[-1])
                                        
        return maxLength
                
             