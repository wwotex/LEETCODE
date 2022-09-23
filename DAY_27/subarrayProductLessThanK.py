from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        left, result, prod = 0, 0, 1
        for right, el in enumerate(nums):
            prod *= el
            while prod >= k and left < len(nums):
                prod /= nums[left]
                left += 1
            result += right - left + 1
        
        return result


sol = Solution()
nums = [3,4,5]
k = 1
print(sol.numSubarrayProductLessThanK(nums, k))

# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         left, right = 0, 0
#         result = 0
#         prod = nums[0]
#         while right < len(nums):
#             if prod < k:
#                 result += right - left + 1
#                 right += 1
#                 if right < len(nums):
#                     prod *= nums[right]
#             else:
#                 prod /= nums[left]
#                 left += 1
#         return result