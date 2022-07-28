class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        k = 1
        n1 = 0
        n2 = 1
        temp = 0
        while k < n:
            k += 1
            temp = n1+n2
            n1 = n2
            n2 = temp

        return temp
        
sol = Solution()
for el in range(20):
    print(sol.fib(el))