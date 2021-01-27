#
# * 121. Best Time to Buy and Sell Stock
# * Easy

# * Say you have an array for which the ith element is the price of a given stock
# * on day i.

# * If you were only permitted to complete at most one transaction (i.e., buy one
# * and sell one share of the stock), design an algorithm to find the maximum
# * profit.

# Note that you cannot sell a stock before you buy one.

# * Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.

# * Example 2:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# %%

class Solution:
    # * Solution 1
    # ! Dynamic programming
    def maxProfit1(self, prices: list) -> int:
        n = len(prices)
        if n == 0:
            return 0

        # * Since only one trading, dp is 2D: 1) day#; 2)whether holding stock
        # k = 2
        dp = [[0, 0] for _ in range(n)]

        # print(dp)
        for i in range(n):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], -prices[i])

        return dp[n-1][0]

    # * Solution 2
    # ! Dynamic programming with compressed DP
    def maxProfit2(self, prices: list) -> int:
        n = len(prices)
        if n == 0:
            return 0

        dp_i_0 = 0
        dp_i_1 = -sum(prices)

        for i in range(n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])

        return dp_i_0


    # * Solution 3
    # ! Kadane Algorithm
    def maxProfit3(self, prices: list)->int:
        n = len(prices)
        if n == 0:
            return 0
        
        maxCurrent = 0
        maxProfit = float('-inf')

        for i in range(1, n):
            maxCurrent += ((prices[i] - prices[i-1]))
            # ! if maxCurrent < 0, we reset it, since min profit can be zero in 
            # ! any situation
            maxCurrent = max(0, maxCurrent)
            maxProfit = max(maxCurrent, maxProfit)
        
        return maxProfit

    # * Solution 4
    # ! Full dimension DP
    def maxProfit4(self, prices: list)-> int:
        n = len(prices)
        if n == 0:
            return 0
        
        K = 1
        # * Set 3d dp, n: day #; k: transaction #; [no stock, hold stock]
        # * all set to not calculated
        dp = [[[float('-inf'), float('-inf')] for __ in range(K+1)] for _ in range(n)]

        # * Base case
        # ! this is simple case, Full case see Q123
        # * For first day, 0 transaction is done: if no stock, profit is 0,
        # * For first day, 1 transaction is done: if hold stock,  -infinity
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]

        print(dp)
        
        for i in range(1, n):
            # * actually k only = 1
            for k in range(1, K+1):
                print(i,k)
                # ! note: when buy stock, transaction # k decrease 1; 
                # !       when sell, k is unchanged
                dp[i][k][0] = max(dp[i-1][k][0], (dp[i-1][k][1] + prices[i]))
                dp[i][k][1] = max(dp[i-1][k][1], (dp[i-1][k-1][0] - prices[i]))
        
        print(dp)
        return dp[n-1][K][0]

                


sol = Solution()
a1 = [7, 1, 5, 3, 6, 4]
r1 = sol.maxProfit4(a1)
print('Expected 5', r1)

# %%

# %%
