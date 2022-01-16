class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        reversed_tokens = []
        stack = []
        for _ in range(len(tokens)):
            reversed_tokens.append(tokens.pop())
        for _ in range(len(reversed_tokens)):
            value = reversed_tokens.pop()
            if value not in ('+', '-', '*', '/'):
                stack.append(int(value))
            else:
                nums1 = int(stack.pop())
                nums2 = int(stack.pop())
                if value == '+':
                    stack.append(nums2+nums1)
                elif value == '-':
                    stack.append(nums2-nums1)
                elif value == '*':
                    stack.append(nums2*nums1)
                elif value == '/':
                    stack.append(nums2/nums1)
        return int(stack.pop())