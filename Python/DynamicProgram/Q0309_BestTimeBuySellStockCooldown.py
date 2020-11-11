#
# * 309. Best Time to Buy and Sell Stock with Cooldown
# * Medium

# * Say you have an array for which the ith element is the price of a given stock on day i.

# * Design an algorithm to find the maximum profit. You may complete as many 
# * transactions as you like (ie, buy one and sell one share of the stock multiple 
# * times) with the following restrictions:

#     You may not engage in multiple transactions at the same time (ie, you must 
#       sell the stock before you buy again).
#     After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

# * Example:

# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

#%%

class Solution:

    # * Solution 1
    def maxProfit1(self, prices: list) -> int:
        n = len(prices)
        if n == 0:
            return 0

        dp = [[0,0] for _ in range(n)]

        for i in range(n):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            elif i == 1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                # ! since i = 1, cannot use i-2
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                # ! Key: since need cooldown for one day, its from i-2
                dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
            
        return dp[n-1][0]



sol = Solution()
a = [1, 2, 3, 0, 2]
r1 = sol.maxProfit1(a)
print(r1)
