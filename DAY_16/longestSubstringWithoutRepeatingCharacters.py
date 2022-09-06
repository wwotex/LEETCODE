
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        H = set()
        best = left = right = 0
        while right < len(s):
            if s[right] not in H:
                best = max(best, right - left + 1)
                H.add(s[right])
                right += 1
            else:
                H.remove(s[left])
                left += 1
        return best

sol = Solution()
str = 'abcaa'
print(sol.lengthOfLongestSubstring(str))