from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)


sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-6,4,1000]
print(sol.maxSubArray(nums))

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         sum_ending_here, max_sum = 0, -float('inf')
#         for el in nums:
#             sum_ending_here += el
#             max_sum = max(max_sum, sum_ending_here)
#             if sum_ending_here < 0:
#                 sum_ending_here = 0

#         return max_sum

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
