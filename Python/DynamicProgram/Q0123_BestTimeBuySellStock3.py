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

        for i in range(n):
            # ! this is also base case, but dp[0][0][1] will never be used,
            # ! so that we can skip this part
            if i == 0:
                dp[i][0][0] = 0
                dp[i][0][1] = float('-inf')
                
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


    # * Solution 2
    # ! simplified, since 0 <= k <=2, list all possible k values
    def maxProfit2(self, prices: list) -> int:
        n = len(prices)
        if n == 0:
            return 0

        dp_i10 = 0
        dp_i20 = 0
        dp_i11 = float('-inf')
        dp_i21 = float('-inf')

        for price in prices:
            dp_i20 = max(dp_i20, dp_i21 + price)
            dp_i21 = max(dp_i21, dp_i10 - price)
            dp_i10 = max(dp_i10, dp_i11 + price)
            dp_i11 = max(dp_i11, -price)

        return dp_i20


    # * Solution 3
    # ! Full dimension DP, More generic form
    def maxProfit3(self, prices: list)-> int:
        n = len(prices)
        if n == 0:
            return 0
        
        K = 2
        # * Set 3d dp, n: day #; k: transaction #; [no stock, hold stock]
        # * all set to not calculated/impossible
        dp = [[[float('-inf'), float('-inf')] for __ in range(K+1)] for _ in range(n)]

        # * Base case
        # * 1) For every day:
        # * 0 transaction is done: 
        # *     if no stock, profit is 0,
        # *     if hold stock, impossible (for 0 transaction)
        for i in range(n):
            dp[i][0][0] = 0

        # * 2) For first day:
        # * 0 transaction is covered above
        # * 1 or more transaction is done:
        # *     if no stock, no profit, it is 0,
        # *     if hold stock, it must buy at first day, profit is -prices[0]
        for k in range(1, K+1):
            dp[0][k][0] = 0
            dp[0][k][1] = -prices[0]

        # print(dp)
        
        for i in range(1, n):
            # * actually k only = 1
            for k in range(1, K+1):
                # print(i,k)
                # ! note: when buy stock, transaction # k decrease 1; 
                # !       when sell, k is unchanged
                dp[i][k][0] = max(dp[i-1][k][0], (dp[i-1][k][1] + prices[i]))
                dp[i][k][1] = max(dp[i-1][k][1], (dp[i-1][k-1][0] - prices[i]))
        
        # print(dp)
        return dp[n-1][K][0]


sol = Solution()
a1 = [3,3,5,0,0,3,1,4]
r1 = sol.maxProfit3(a1)
print('Expected 6', r1)

a1 = [1,2,3,4,5]
r1 = sol.maxProfit3(a1)
print('Expected 4', r1)

a1 = [7,6,4,3,1]
r1 = sol.maxProfit3(a1)
print('Expected 0', r1)

a1 = [14,9,10,12,4,8,1,16]
r1 = sol.maxProfit3(a1)
print('Expected 19', r1)

# r2 = sol.maxProfit1(a1)
# print('Expected 19', r2)

# %%
