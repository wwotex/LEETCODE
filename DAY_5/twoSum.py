from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        for i, el in enumerate(nums):
            if (target - el) in D:
                a1 = D[target-el]
                a2 = i
                return [a1, a2]
            if el not in D:
                D[el] = i
            

sol = Solution()
ls = [3,2,4]
tar = 6
print(sol.twoSum(ls, tar))