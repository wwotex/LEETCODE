from turtle import color
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        colors += '1'
        neededTime.append(-60)
        result, max_time, color_sum, curr_color = 0, neededTime[0], neededTime[0], colors[0]
        for i in range(1, len(colors)):
            if colors[i] == curr_color:
                color_sum += neededTime[i]
                max_time = max(max_time, neededTime[i])
            else:
                result += color_sum - max_time
                color_sum = max_time = neededTime[i]
            curr_color = colors[i]
        return result

sol = Solution()
colors = "aabaa"
neededTime = [1,2,3,4,1]
print(sol.minCost(colors, neededTime))