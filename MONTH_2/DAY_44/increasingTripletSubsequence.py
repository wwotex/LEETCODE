from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for el in nums:
            if el <= first:
                first = el
            elif el <= second:
                second = el
            else:
                return True

        return False

sol = Solution()
nums = [4,5,2147483647,1,2]
print(sol.increasingTriplet(nums))