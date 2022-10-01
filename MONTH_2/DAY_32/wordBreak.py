from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        LEN = len(s)
        wordDict = set(wordDict)
        possible_so_far = [LEN]

        for x in range(LEN-1, -1, -1):
            for y in possible_so_far:
                if s[x:y] in wordDict:
                    possible_so_far.append(x)
                    break
        return possible_so_far[-1] == 0

sol = Solution()
s = 'leetcode'
wordDict = ['le', 'leet', 'etco', 'ode']
print(sol.wordBreak(s, wordDict))