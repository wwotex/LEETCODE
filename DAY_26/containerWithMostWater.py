from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) -1
        result = 0
        while left < right:
            result = max(result, )
        
sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height))