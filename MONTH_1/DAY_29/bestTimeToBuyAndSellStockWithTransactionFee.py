from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        holding, not_holding = -float('inf'), 0
        for el in prices:
            tempH = holding
            holding = max(holding, not_holding - el)
            not_holding = max(not_holding, tempH + el - fee)
            pass
        return not_holding
    

sol = Solution()
prices = [1,2,3,4,5,6,1,2,3,4,5,100]
fee = 6
print(sol.maxProfit(prices, fee))

