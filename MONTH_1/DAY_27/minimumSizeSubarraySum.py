from cmath import inf
import enum
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, sum, min_window = 0, 0, float('inf')
        for right, el in enumerate(nums):
            sum += el
            while sum >= target:
                min_window = min(min_window, right - left + 1)
                sum -= nums[left]
                left += 1
        return min_window if min_window < float('inf') else 0
