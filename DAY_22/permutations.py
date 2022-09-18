from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        S = [([], nums)]
        while S:
            (used, left) = S.pop()
            if len(used) == len(nums):
                result.append(used)
                continue

            for i, el in enumerate(left):
                new = left.copy()
                new.pop(i)
                S.append((used+[el], new))
        return result

sol = Solution()
nums = [1]
print(sol.permute(nums))