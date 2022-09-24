from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                result += prices[i] - prices[i-1]
        return result

sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         result = 0
#         trend_up = True
#         last_peak = prices[0]
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i-1] and trend_up == False: 
#                 last_peak = prices[i-1]
#                 trend_up = True
#             elif prices[i] < prices[i-1] and trend_up == True:
#                 result += prices[i-1] - last_peak
#                 trend_up = False

#         if trend_up: result += prices[-1] - last_peak
#         return result