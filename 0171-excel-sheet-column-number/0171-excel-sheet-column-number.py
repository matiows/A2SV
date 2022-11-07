class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column = 0
        for ch in columnTitle:
            column = column * 26 + ord(ch) - 64
        return column