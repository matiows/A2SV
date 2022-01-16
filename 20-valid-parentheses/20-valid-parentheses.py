class Solution:
    def isValid(self, s: str) -> bool:
        flag = 0
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append (ch)
            elif len(stack) > 0:
                last = stack[len(stack)-1]                
                if ord(last) == ord(ch)-1 or ord(last) == ord(ch)-2:
                    stack.pop()
                else:
                    flag = 1
                    break
            else:
                flag = 1
                break
        if len(stack) == 0 and flag == 0:
            return True
        else:
            return False