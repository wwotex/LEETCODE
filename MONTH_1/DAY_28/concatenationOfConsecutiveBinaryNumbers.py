class Solution:
    def concatenatedBinary(self, n: int) -> int:
        multiplier = 2
        result = 0
        for el in range(1,n+1):
            if el >= multiplier: multiplier *= 2
            result = (result*multiplier + el) % (1000000007)
        return result

sol = Solution()

n = 12


print(sol.concatenatedBinary(n))