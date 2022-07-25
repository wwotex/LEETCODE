from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0
        for i, el in enumerate(nums):
            if leftsum == (S - el - leftsum):
                return i
            leftsum += el
        return -1


input = [-1,-1,0,1,1,0]
sol = Solution()
print(sol.pivotIndex(input))