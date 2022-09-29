from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        highest_right_wall = [0 for el in height]
        for i in range(len(height)-2, -1, -1):
            highest_right_wall[i] = max(height[i+1], highest_right_wall[i+1])
        
        result = 0
        heighest_left_wall = height[0]
        for i in range(1, len(height)):
            heighest_left_wall = max(heighest_left_wall, height[i])
            result += max(0, min(heighest_left_wall, highest_right_wall[i]) - height[i])
        print(highest_right_wall)
        return result

sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(height))
print(2 + 1 + 4 + 2)