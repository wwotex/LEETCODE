import enum
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p = 0
        q = len(nums)-1
        while p <= q:
            m = p + (q-p)//2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                q = m-1
            else:
                p = m+1
        return -1

sol = Solution()
ls = [-1,0,3,5,9,12]
for i, el in enumerate(ls):
    print(f'el = {el}')
    assert (i == sol.search(ls, el))

print(sol.search(ls, -2))
print(sol.search(ls, 1))
print(sol.search(ls, 4))
print(sol.search(ls, 6))
print(sol.search(ls, 10))
print(sol.search(ls, 16))
        