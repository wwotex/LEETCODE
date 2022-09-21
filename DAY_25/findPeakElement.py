from collections import deque
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left) // 2

            if nums[mid+1] > nums[mid]:
                left = mid+1
            else:
                right = mid
        return left

sol = Solution()
nums = [3,4,3,2,1]
print(sol.findPeakElement(nums))
deq = deque(nums)
for x in range(len(nums)):
    nums = list(deq)
    print(nums)
    print(sol.findPeakElement(nums))
    deq.rotate(1)