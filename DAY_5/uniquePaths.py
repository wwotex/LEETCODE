import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        top = math.factorial(m + n - 2)
        bottom = math.factorial(n - 1)*math.factorial(m - 1)
        return int(top/bottom)