class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        _sum = 0
        for val in ops:
            if val == 'C':
                stack.pop()
            elif val == 'D':
                temp = stack.pop()
                stack.append(temp)
                stack.append (temp*2)
            elif val == '+':
                nums1 = stack.pop()
                nums2 = stack.pop()
                stack.append (nums2)
                stack.append (nums1)
                stack.append (nums1 + nums2)
            else:
                stack.append(int(val))
        for val in stack:
            _sum += int(val)
        return _sum