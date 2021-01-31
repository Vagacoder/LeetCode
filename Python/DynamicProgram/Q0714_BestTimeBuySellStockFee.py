#
# * 714. Best Time to Buy and Sell Stock with Transaction Fee
# * Medium

# * Your are given an array of integers prices, for which the i-th element is the 
# * price of a given stock on day i; and a non-negative integer fee representing 
# * a transaction fee.

# * You may complete as many transactions as you like, but you need to pay the 
# * transaction fee for each transaction. You may not buy more than 1 share of a 
# * stock at a time (ie. you must sell the stock share before you buy again.)

# Return the maximum profit you can make.

# * Example 1:

# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1
# Selling at prices[3] = 8
# Buying at prices[4] = 4
# Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

# * Note:
# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.

#%%

class Solution:
    # * Solution 1
    # * Take fee at selling
    def maxProfit1(self, prices: list, fee: int) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        dp = [[0,0] for _ in range(n)]

        for i in range(n):
            # * Base case
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            else:
                # ! NOTE: reduce fee at selling
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        
        # print(dp)

        return dp[n-1][0]            

    # * Solution 2
    # * take fee at buing
    def maxProfit2(self, prices: list, fee: int) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        dp = [[0,0] for _ in range(n)]

        for i in range(n):
            # * Base case
            if i == 0:
                dp[i][0] = 0
                # ! NOTE: reduce fee at buying
                dp[i][1] = -prices[i] - fee
            else:
                # ! NOTE: reduce fee at buying
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
        
        # print(dp)

        return dp[n-1][0]     



sol = Solution()
prices = [1, 3, 2, 8, 4, 9]
fee = 2
r1 = sol.maxProfit1(prices, fee)
print(r1)
r2 = sol.maxProfit2(prices, fee)
print(r2)

# %%
