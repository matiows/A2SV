class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return '0'
        
        stack = []
        
        for c in num:
            while len(stack) > 0 and k > 0 and c < stack[-1]:
                k -= 1
                stack.pop()
            stack.append(c)
            
        stack = stack[:len(stack) - k]
        
        return str(int(''.join(stack)))