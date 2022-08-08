class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_reg = [0 for x in range(10)]
        guess_reg = secret_reg.copy()
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_reg[int(s)] += 1
                guess_reg[int(g)] += 1

        for s, g in zip(secret_reg, guess_reg):
            cows += min(s, g)
        
        return f'{bulls}A{cows}B'

sol = Solution()
secret = "1123"
guess = "0111"
print(sol.getHint(secret, guess))