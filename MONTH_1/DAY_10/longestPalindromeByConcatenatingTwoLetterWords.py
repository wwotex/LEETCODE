class Solution:
    def longestPalindrome(self, words):
        D = {}
        for el in words:
            if el in D:
                D[el] += 1
            else:
                D[el] = 1

        result = 0
        wasAdditional = 0
        for str in D:
            rev = str[::-1]
            if rev == str:
                c = D[str]
                rem = c % 2
                if rem == 1 and not wasAdditional:
                    wasAdditional = 1
                result += 2*( c - rem )

            elif D.get(rev):
                c1, c2 = D[str], D[rev]
                D[rev] = 0
                D[str] = 0
                result += 4*min(c1, c2)
        return result + 2*wasAdditional

sol = Solution()
words = ["lc","cl","gg"]
print(sol.longestPalindrome(words))