class Solution:
    def climbStairs(self, n: int) -> int:
        n+=1

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
        