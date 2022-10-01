from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3: return 0
        result = 0
        diff, left = nums[1] - nums[0], 0
        for right in range(1, len(nums)):
            new_diff = nums[right] - nums[right-1]
            while new_diff != diff:
                left += 1
                diff = nums[left+1] - nums[left]

            else:
                result += (right-left-1)
        return result

sol = Solution()
nums = [6,32,1,2,4,6,8]
print(sol.numberOfArithmeticSlices(nums))