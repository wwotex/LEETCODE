class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i, el in enumerate(nums):
            if el > 0 or i >= len(nums)-1: break
            
            if i == 0 or nums[i-1] != el:
                self.twoSum(nums, i+1, el, res)

        return res

    def twoSum(self, nums, i, compliment, res):
        left, right = i, len(nums) - 1
        seen = set()
        while left < right:
            curr_sum = nums[left] + nums[right]
            
            if curr_sum < -compliment:
                left += 1
            elif curr_sum > -compliment:
                right -= 1
            else:
                res.append([compliment, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
        return res

sol = Solution()
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]

print(sol.threeSum(nums))