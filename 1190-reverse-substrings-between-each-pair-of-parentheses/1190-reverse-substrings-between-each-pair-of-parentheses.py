class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for ch in s:
            if ch != ')':
                stack.append(ch)
                
            else:
                temp = []
                value = stack.pop()
                
                while value != '(':
                    temp.append(value)
                    value = stack.pop()
                    
                i = 0
                while i < len(temp):
                    stack.append(temp[i])
                    i+=1
                    
        return (''.join(stack))