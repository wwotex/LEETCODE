from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = 100000
        for el in prices:
            if el < buy_price:
                buy_price = el
            elif (el-buy_price) > max_profit:
                max_profit = (el-buy_price)
        
        return max_profit

sol = Solution()

prices = [7,2,4,600,3,10]
print(sol.maxProfit(prices))