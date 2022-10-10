class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        answer = ''
        for i, el in enumerate(palindrome):
            if len(palindrome) % 2 != 0 and i == len(palindrome) // 2:
                continue
            temp = ''
            if el == 'a':
                temp = palindrome[:i] + 'b' + palindrome[i+1:]
            else:
                temp = palindrome[:i] + 'a' + palindrome[i+1:]
            
            answer = min(answer, temp) if answer != '' else temp

        return answer

sol = Solution()
pal = 'aba'
print(sol.breakPalindrome(pal))
