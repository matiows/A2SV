class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        def isValid(idx, stack):
            if idx == len(s):
                return len(stack) == 0
            
            if (idx, tuple(stack)) in memo:
                return memo[(idx, tuple(stack))]
            
            ch = s[idx]    
            if ch == '(':
                stack.append(ch)
                return isValid(idx + 1, stack)
            
            elif ch == ')':
                if stack:
                    stack.pop()
                    return isValid(idx + 1, stack)
                
                return False
            
            else:
                empty = isValid(idx + 1, stack.copy())
                
                closing = False
                if stack:
                    closing = isValid(idx + 1, stack.copy()[:-1])
                
                opening = isValid(idx + 1, stack + ['('])
                
                memo[(idx, tuple(stack))] = empty or opening or closing
                return empty or opening or closing
            
        return isValid(0, [])
