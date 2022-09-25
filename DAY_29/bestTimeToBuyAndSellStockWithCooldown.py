from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # FSM -> S0 when you just went through cooldown and can buy, S1 bought and can sell, S2 when you sold and experience cooldown
        not_holding, holding, cooldown = 0, -float('inf'), 0
        for el in prices:
            tempS1 = holding
            holding = max(holding, not_holding - el)
            not_holding = max(not_holding, cooldown)
            cooldown = tempS1 + el
            pass
        return max(not_holding, cooldown)

sol = Solution()
prices = [2,4,6,10,1,3,6,10]
print(sol.maxProfit(prices))

