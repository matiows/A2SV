class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = ''
        if len(a) > len(b):
            b = '0'*(len(a) - len(b)) + b
        elif len(b) > len(a):
            a = '0'*(len(b) - len(a)) + a
        result = [''] * len(a)
        for i in range(len(a)-1, -1, -1):
            x = int(a[i])
            y = int(b[i])
            result[i] = str((x ^ y ^ carry))
            if [x, y, carry].count(1) > 1:
                carry = 1
            else:
                carry = 0
        if carry == 1:
            ans = '1' + ''.join(result)
        else:
            ans = ''.join(result)
        return ans