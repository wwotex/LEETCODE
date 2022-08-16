class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = n2 = 0
        for i, el1 in enumerate(reversed(num1)):
            n1 += 10**i * int(el1)
        for i, el2 in enumerate(reversed(num2)):
            n2 += 10**i * int(el2)
        return str(n1*n2)

sol = Solution()
print(sol.multiply('123','23'))