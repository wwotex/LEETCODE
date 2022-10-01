from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = [False for el in nums]
        stamina = 1
        for i, el in enumerate(nums):
            if stamina > 0: 
                res[i] = True
                stamina -= 1 
                stamina = max(stamina, el)

        return res[-1]        

sol = Solution()
nums = [2,0,2,3,4]
print(sol.canJump(nums))