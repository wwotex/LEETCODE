from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) -1
        result = 0
        while left < right:
            result = max(result, (right-left)*( min(height[left], height[right]) ))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result
        
sol = Solution()
height = [1,8,6,1000,1,1000,8,3,7]
print(sol.maxArea(height))