from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        curr_start, alternative = 0, 0
        sign = 0
        longest = 0
        for i, el in enumerate(nums):
            if el > 0:
                if sign == 0:
                    sign = 1
            elif el == 0:
                sign = 0
                curr_start = i+1
                alternative = i+1
            else:
                if sign == 0: sign = 1
                sign *= (-1)
                if alternative == curr_start:
                    alternative = i+1

            if sign > 0:
                longest = max(longest, i - curr_start + 1)
            elif curr_start < alternative <= i and sign < 0:
                longest = max(longest, i - alternative + 1)

        return longest

sol = Solution()
nums = [-16,0,-5,2,2,-13,11,8]
print(sol.getMaxLen(nums))

