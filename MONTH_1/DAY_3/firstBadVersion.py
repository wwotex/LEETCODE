global n, b 
# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    global n, b 
    if version >= b:
        return True
    else:
        return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        p, q = 1, n
        while p <= q:
            m = p + (q-p)//2
            if isBadVersion(m):
                q = m - 1
            else:
                p = m + 1
        return p

sol = Solution()
n = 5
b = 4

for el in range(1,n+1):
    b = el
    print(f'asserting {el}')
    assert sol.firstBadVersion(n) == b
