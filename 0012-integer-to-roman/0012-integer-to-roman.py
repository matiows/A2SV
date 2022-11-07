class Solution:
    def intToRoman(self, n: int) -> str:
        r = ''
        while True:
            if n - 1000 > -1:
                r += 'M'
                n -= 1000
            elif n - 900 > -1:
                r += 'CM'
                n -= 900
            elif n - 500 > -1:
                r += 'D'
                n -= 500
            elif n - 400 > -1:
                r += 'CD'
                n -= 400
            elif n - 100 > -1:
                r += 'C'
                n -= 100
            elif n - 90 > -1:
                r += 'XC';
                n -= 90
            elif n - 50 > -1:
                r += 'L'
                n -= 50
            elif n - 40 > -1:
                r += 'XL'
                n -= 40
            elif n - 10 > -1:
                r += 'X'
                n -= 10
            elif n - 9 > -1:
                r += 'IX'
                n -= 9
            elif n - 5 > -1:
                r += 'V'
                n -= 5
            elif n - 4 > -1:
                r += 'IV'
                n -= 4
            elif n - 1 > -1:
                r += 'I'
                n -= 1
            else:
                break
        return r