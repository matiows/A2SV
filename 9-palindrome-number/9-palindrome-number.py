class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_array = list(str(x))
        x_array_reverse = x_array[::-1]
        if x_array == x_array_reverse:
            return True
        return False
