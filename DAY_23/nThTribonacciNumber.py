class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        t0, t1, t2 = 0, 1, 1
        k = 2
        while k < n:
            temp = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = temp
            k += 1
        return t2