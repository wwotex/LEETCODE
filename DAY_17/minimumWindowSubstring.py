from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        D = Counter(t)
        LEN_T, LEN_S = len(t), len(s)
        left, right = 0, 0
        D[s[0]] -= 1
        minResult = float('inf')
        result = ''
        while left <= right and right < LEN_S:
            consists = True
            for letter, need in D.items():
                if need > 0:
                    consists = False
            if consists:
                if (right - left + 1) < minResult:
                    minResult = (right - left + 1)
                    result = s[left:right+1]

                if s[left] in D: D[s[left]] += 1
                left += 1
            else:
                right += 1
                if right < LEN_S and s[right] in D: D[s[right]] -= 1

        return result

sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(sol.minWindow(s,t))