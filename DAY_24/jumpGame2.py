from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = [-1 for el in nums]
        curr_step = 0
        curr_stamina = 1
        next_stamina = 1
        for i in range(len(nums)):
            
            if curr_stamina > 0:
                curr_stamina -= 1
                next_stamina -= 1
                next_stamina = max(next_stamina, nums[i])
            else:
                curr_stamina = next_stamina - 1
                next_stamina = nums[i]
                curr_step += 1
                
            
            steps[i] = curr_step
            
            

        return steps[-1]      

sol = Solution()
nums = [3,2,0,2,3,1,1,1]
print(nums)
print(sol.jump(nums))