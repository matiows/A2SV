class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        reversed_tokens = []
        for _ in range(len(tokens)):
            reversed_tokens.append(tokens.pop())
        while len(reversed_tokens) > 1:
            temp = []
            nums1 = int(reversed_tokens.pop())
            nums2 = int(reversed_tokens.pop())
            value = reversed_tokens.pop()
            while value not in ('+', '-', '*', '/') :
                temp.append(nums1)
                nums1 = nums2
                nums2 = int(value)
                value = reversed_tokens.pop()
            if value == '+':
                reversed_tokens.append(nums1+nums2)
            elif value == '-':
                 reversed_tokens.append(nums1-nums2)
            elif value == '*':
                 reversed_tokens.append(nums1*nums2)
            elif value == '/':
                 reversed_tokens.append(nums1/nums2)
            while len(temp) != 0:
                reversed_tokens.append(temp.pop())
        return int(reversed_tokens.pop())