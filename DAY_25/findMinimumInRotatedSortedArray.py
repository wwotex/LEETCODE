from collections import deque
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[left] <= nums[right]:
                return nums[left]
            elif nums[mid] >= nums[left]:
                left = mid+1
            else:
                right = mid
        

sol = Solution()
nums = [1]
deq = deque(nums)
for x in range(len(nums)):
    nums = list(deq)
    print(sol.findMin(nums))
    deq.rotate(1)

# print(sol.findMin(nums))