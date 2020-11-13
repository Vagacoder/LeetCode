#
# * 188. Best Time to Buy and Sell Stock IV
# ! Hard

# * You are given an integer array prices where prices[i] is the price of a given 
# * stock on the ith day.

# Design an algorithm to find the maximum profit. 
# ! You may complete at most k transactions.

# Notice that you may not engage in multiple transactions simultaneously (i.e., 
# you must sell the stock before you buy again).

 

# * Example 1:

# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

# * Example 2:

# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 
# 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

 

# * Constraints:

#     0 <= k <= 109
#     0 <= prices.length <= 1000
#     0 <= prices[i] <= 1000

#%%
class Solution:

    # * Solution 1
    # * copy from Q123
    def maxProfit1(self, k: int, prices: list) -> int:
        n = len(prices)
        if n == 0:
            return 0;
        
        dp = [[[0,0] for __ in range(k+1)] for _ in range(n)]

        sumPrice = sum(prices)

        for i in range(n):
            if i == 0:
                dp[i][0][0] = 0
                dp[i][0][1] = -sumPrice

            for j in range(k, 0, -1):
                if i == 0:
                    dp[i][j][0] = 0;
                    dp[i][j][1] = -prices[i]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
                

        return dp[n-1][k][0]


sol = Solution()
k = 2
prices = [3,2,6,5,0,3]
r1 = sol.maxProfit1(k, prices)
print(r1)

k = 2
prices = [2,4,1]
r1 = sol.maxProfit1(k, prices)
print(r1)

# %%