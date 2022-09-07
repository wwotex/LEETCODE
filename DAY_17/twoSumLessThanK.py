class Solution:
    def twoSumLessThanK(self, nums, k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        best_sum = -1
        while left != right:
            curr_sum = nums[left] + nums[right]
            if curr_sum < k:
                best_sum = max(best_sum, curr_sum)
                left += 1
            else:
                right -= 1
        return best_sum

sol = Solution()
nums = [254,914,110,900,147,441,209,122,571,942,136,350,160,127,178,839,201,386,462,45,735,467,153,415,875,282,204,534,639,994,284,320,865,468,1,838,275,370,295,574,309,268,415,385,786,62,359,78,854,944]
k = 200
print(sol.twoSumLessThanK(nums, k))