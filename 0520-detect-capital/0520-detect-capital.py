class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        check = ord(word[0]) < 96
        if len(word) == 1:
            return True
        if check and ord(min(word[1:])) > 96:
            return True
        if ord(max(word)) < 96:
            return True
        if ord(min(word)) > 96:
            return True
        return False
        