class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        length = len(strs[0])
        count = 0
        for i in range(length):
            prev = ""
            for word in strs:
                if prev <= word[i]:
                    prev = word[i]
                else:
                    count += 1
                    break
        return count
                