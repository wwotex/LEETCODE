from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i, el in enumerate(cost):
            if i > 1:
                cost[i] = min(el+cost[i-1], el+cost[i-2])

        return cost.pop()

sol = Solution()
ls = [1,100,1,1,1,100,1,1,100,1]
print(sol.minCostClimbingStairs(ls))