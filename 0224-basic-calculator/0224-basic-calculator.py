class Solution:
    def calculate(self, s: str) -> int:
        exp = list(s)
        space = []
        
        for v in exp:
            if v == ' ':
                continue
            space.append(v)
            
        stack = []
        num = 0
        total = 0
        sign = 1
        
        for val in space:
            if val.isdigit():
                num *= 10
                num += int(val)
            
            elif val=='+':
                total+= num*sign
                num = 0
                sign = 1
            elif val=='-':
                total+=num*sign
                num = 0
                sign = -1
            elif val=='(':
                stack.append(total)
                stack.append(sign)
                sign = 1
                total = 0
            elif val==')':
                total += sign * num
                num = 0
                total *= stack.pop()
                total += stack.pop()
        
        if num != 0:
            total += num * sign
        return total