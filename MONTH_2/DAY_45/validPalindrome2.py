class Solution:
    def validPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s)-1
        while p1 < p2:
            if s[p1] != s[p2]:
                opt1, opt2 = s[p1+1:p2+1], s[p1:p2]
                return opt1 == opt1[::-1] or opt2 == opt2[::-1]
            else:
                p1 += 1
                p2 -= 1

        return True

sol = Solution()
s = "acxcybycxcxa"
print(sol.validPalindrome(s))