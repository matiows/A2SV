class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        ans = 0
        for value in count.values():
            ans += value // 2 * 2
            if value % 2 != 0 and ans %2 == 0:
                ans += 1
        return ans
        