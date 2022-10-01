import math

class Solution:
    def maxProduct(self, nums) -> int:
        last_min = last_max = result = nums[0]
        
        for x in range(1, len(nums)):
            temp = max(nums[x], last_min*nums[x], last_max*nums[x])
            last_min = min(nums[x], last_min*nums[x], last_max*nums[x])
            last_max = temp
            result = max(result, last_max)
        return result

 
# my weird solution
# class Solution:
#     def maxProduct(self, nums) -> int:
#         def maxProductNonZero(nums):
#             if not nums:
#                 return -float('inf')
#             if len(nums) == 1:
#                 return nums[0]
#             negatives = [i for i, el in enumerate(nums) if el < 0 ]
#             if len(negatives) % 2 == 0:
#                 return math.prod(nums)
#             elif len(negatives) == 1:
#                 left = math.prod(nums[:negatives[0]])
#                 right = math.prod(nums[negatives[-1]+1:])
#                 if negatives[0] == 0:
#                     return right
#                 if negatives[0] == (len(nums)-1):
#                     return left
#                 return left if left > right else right
#             else:
#                 mid = math.prod( nums[negatives[0]+1 : negatives[-1]] )
#                 left = math.prod(nums[:negatives[0]+1])
#                 right = math.prod(nums[negatives[-1]:])
#                 return left * mid if left < right else right * mid

#         zeros = [i for i, el in enumerate(nums) if el == 0]
#         if len(zeros) == 0:
#             return maxProductNonZero(nums)
#         best = 0
#         last_x = -1
#         zeros.append(len(nums))
#         for x in zeros:
#             temp = maxProductNonZero(nums[last_x+1:x])
#             if temp > best:
#                 best = temp
#             last_x = x
#         return best


sol = Solution()
nums = [-1,-2,-9,-6]
print(sol.maxProduct(nums))