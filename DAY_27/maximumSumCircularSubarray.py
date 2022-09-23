from tkinter import N
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kandane(nums: List[int]) -> int:
            sum_ending_here, max_sum = 0, -float('inf')
            for i in range(len(nums)):
                sum_ending_here += nums[i]
                max_sum = max(sum_ending_here, max_sum)
                sum_ending_here = max(0, sum_ending_here)
            return max_sum
        
        result = max(kandane(nums), sum(nums) + kandane([-x for x in nums]))
        return result if result > 0 else max(nums)


sol = Solution()
nums = [5,-3,5]
# nums = [-2,1,-3,4,-1,2,1,-6,4,1000]
print(sol.maxSubarraySumCircular(nums))

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         left, sum, max_sum = 0, 0, -float('inf')
#         for right, el in enumerate(nums):
#             sum += el
#             max_sum = max(max_sum, sum)
#             while (sum < 0 or nums[left] < 0) and left < right:
#                 sum -= nums[left]
#                 max_sum = max(max_sum, sum)
#                 left += 1
#         return max_sum
