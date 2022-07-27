class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_occurrences = [0] * 123
        for el in s:
            letter_occurrences[ord(el)] += 1
        
        palindrome_len = 0
        one_odd = 0
        for el in letter_occurrences:
            adding = 2*int(el/2)
            palindrome_len += adding
            el -= adding
            if el > 0:
                one_odd = 1
        
        return palindrome_len + one_odd

sol = Solution()

S = "bbbcc"
print(sol.longestPalindrome(S))