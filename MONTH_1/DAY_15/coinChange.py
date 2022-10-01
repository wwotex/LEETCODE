class Solution:
    def coinChange(self, coins, amount: int) -> int:
        min_count = [float('inf') for el in range(amount + 1)]
        min_count[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                min_count[i] = min(min_count[i], min_count[i - coin] + 1)
        return min_count[amount] if min_count[amount] != float('inf') else -1 


# class Solution:
#     def coinChange(self, coins, amount: int) -> int:
#         min_count = [-1 for el in range(amount+1)]
#         min_count[0] = 0
#         for i in range(amount+1):
#             for coin in coins:
#                 if i - coin >= 0 and min_count[i-coin] >= 0:
#                     min_count[i] = min(min_count[i], min_count[i-coin] + 1) if min_count[i] >= 0 else (min_count[i-coin] + 1)
#         return min_count[amount] 
            

sol = Solution()
coins = [186,419,83,408]
amount = 6249
print(sol.coinChange(coins, amount))