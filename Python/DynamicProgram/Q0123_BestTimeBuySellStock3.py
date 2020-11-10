#
# * 123. Best Time to Buy and Sell Stock
# ! Hard

# * Say you have an array for which the ith element is the price of a given stock 
# * on day i.

# * Design an algorithm to find the maximum profit. You may complete at most two 
# * transactions.

# * Note: You may not engage in multiple transactions at the same time (i.e., you 
# * must sell the stock before you buy again).

 

# * Example 1:

# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

# * Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are 
# engaging multiple transactions at the same time. You must sell before buying again.

# * Example 3:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# * Example 4:

# Input: prices = [1]
# Output: 0

# * Constraints:

#     1 <= prices.length <= 105
#     0 <= prices[i] <= 105

#%%

class Solution:

    # * Solution 1
    def maxProfit1(self, prices: list) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        max_k = 2

        dp = [[[0, 0] for __ in range(max_k+1)] for _ in range(n)]

        # print(dp)

        sumPrice = sum(prices)

        for i in range(n):
            # ! this is also base case, but dp[0][0][1] will never be used,
            # ! so that we can skip this part
            if i == 0:
                dp[i][0][0] = 0
                dp[i][0][1] = -sumPrice
                
            for k in range(max_k, 0, -1):
                # ! KEY ! must know how to calculate base case
                if i == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    print(dp)
                else:
                    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        
        print(dp)

        return dp[n-1][max_k][0]




sol = Solution()
a1 = [3,3,5,0,0,3,1,4]
r1 = sol.maxProfit1(a1)
print(r1)


# %%
