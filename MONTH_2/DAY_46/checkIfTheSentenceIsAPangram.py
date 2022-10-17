from collections import Counter


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        D = Counter(sentence)
        return len(D) == 26

sol = Solution()
sentence = "thequickbrownfoxjumpsoverthelazydog"
# sentence = 'leetcode'
print(sol.checkIfPangram(sentence))