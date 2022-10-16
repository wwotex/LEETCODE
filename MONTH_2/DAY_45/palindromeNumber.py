from unicodedata import digit


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        digits = []
        while x:
            digits.append(x % 10)
            x //= 10

        L2 = len(digits) // 2
        for i, el in enumerate(digits[:L2]):
            if el != digits[-(i+1)]:
                return False

        return True

sol = Solution()

x = 122
print(sol.isPalindrome(x))