class Solution:
    def maximum69Number (self, num: int) -> int:
        text = str(num)
        text2 = text.replace("6", "9", 1)
        return max(text,text2)