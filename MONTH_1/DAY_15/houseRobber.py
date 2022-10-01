class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        for i in range(n):
            if i == 1:
                nums[i] = max(nums[i-1], nums[i])
            elif i > 1:
                nums[i] = max(nums[i-1], nums[i-2] + nums[i])
        return nums[n-1]