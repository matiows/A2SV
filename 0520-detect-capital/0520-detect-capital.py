class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        check = ord(word[0]) < 96
        caps = 0
        for ch in word:
            if ord(ch) < 96:
                caps += 1
        if caps == len(word) or caps == 0:
            return True
        return caps == 1 and check
        