from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        LEN = len(nums)
        if LEN <= 3: return max(nums)
        laster, last, laster2, last2 = nums[0], max(nums[0], nums[1]), nums[1], max(nums[1], nums[2])
        for x in range(2, LEN):
            if x != LEN - 1:
                temp = max(laster + nums[x], last)
                laster = last
                last = temp
            
            if x != 2:
                temp = max(laster2 + nums[x], last2)
                laster2 = last2
                last2 = temp
        return max(last, last2)
            
sol = Solution()
nums = [1,3,1,3,100]
print(sol.rob(nums))