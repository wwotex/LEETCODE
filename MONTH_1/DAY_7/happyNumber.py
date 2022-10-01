class Solution:
    def isHappy(self, n: int) -> bool:
        D = {}
        while n != 1:
            if n in D:
                return False
            D[n] = 1
            new = 0
            while n:
                d = n % 10
                # print(f'digit: {d}')
                new += d**2
                n //= 10
            # print(f'new: {new}')
            n = new
                   
        return True

sol = Solution()
n = 2
print(sol.isHappy(n))