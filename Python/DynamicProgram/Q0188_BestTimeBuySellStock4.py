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
import math

class Solution:

    # * Solution 1
    # * copy from Q123, Dynamic Programming
    def maxProfit1(self, k: int, prices: list) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0;
        
        dp = [[[0,0] for __ in range(k+1)] for _ in range(n)]

        # sumPrice = sum(prices)

        for i in range(n):
            if i == 0:
                dp[i][0][0] = 0
                dp[i][0][1] = float('-inf')

            for j in range(k, 0, -1):
                if i == 0:
                    dp[i][j][0] = 0;
                    dp[i][j][1] = -prices[i]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
                

        return dp[n-1][k][0]


    # * Solution 2
    # ! From Leetcode solution, Dynamic Programming
    def maxProfit2(self, k: int, prices: list) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        
        # ? if k*2 > n, it suggests that we can buy/sell everyday, which is no limit on k
        # * here we use Greedy Algorithm from Q122
        if (2 * k) > n:
            result = 0
            for i in range(1, n):
                result += max(0, prices[i] - prices[i-1])

            return result

        # ? when k*2 < n

        # * float('-inf') for impossible situation/not calculated yet
        dp = [[[float('-inf'), float('-inf')] for _ in range(k+1)] for __ in range(n)]
        # print(dp)

        # ? base cases:
        # * first day, no transaction is done, no stock in hand
        dp[0][0][0] = 0
        # * first day, did one transaction, stock in hand
        dp[0][1][1] = -prices[0]

        for i in range(1, n):
            for j in range(k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                # ! when j = 0 ,j-1 cannot be negative, 
                # ! this means: you can't hold stock without transaction
                if j > 0:
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

        print(dp)

        # return dp[n-1][k][0]

        result = 0
        for j in range(k+1):
            result = max(result, dp[n-1][j][0])
        
        return result


    # * Solution 3
    # ! From Leetcode solution, Merging
    def maxProfit2(self, k: int, prices: list) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        # * find all consecutively increasing subsequence
        transactions = []
        start = 0
        end = 0
        for i in range(1, n):
            if prices[i] >= prices[i-1]:
                end = i
            else:
                if end > start:
                    transactions.append([start, end])
                start = i

        if end > start:
            transactions.append([start, end])

        # * iterate and merge transactions
        while len(transactions) > k:
            # * check delete loss
            delte_index = 0
            min_delete_loss = math.inf
            for i in range(len(transactions)):
                t = transactions[i]
                profit_loss = prices[t[1] - prices[t[0]]]
                if profit_loss < min_delete_loss:
                    min_delete_loss = profit_loss
                    delete_index = i

            # * check merge loss
            merge_index = 0
            min_merge_loss = math.inf
            for i in range(1, len(transactions)):
                t1 = transactions[i-1]
                t2 = transactions[i]
                profit_loss = prices[t1[1]] - prices[t2[0]]
                if profit_loss < min_merge_loss:
                    min_merge_loss = profit_loss
                    merge_index = i

            # * delete or merge
            if min_delete_loss <= min_merge_loss:
                transactions.pop(delete_index)
            else:
                transactions[merge_index - 1][1] = transactions[merge_index][1]
                transactions.pop(merge_index)

        return sum(prices[j] - prices[i] for i, j in transactions)
    


sol = Solution()

# k = 2
# prices = [3,2,6,5,0,3]
# r1 = sol.maxProfit2(k, prices)
# print(r1)

# k = 2
# prices = [2,4,1]
# r1 = sol.maxProfit2(k, prices)
# print(r1)

# k = 2
# prices = [6,1,3,2,4,7]
# r1 = sol.maxProfit2(k, prices)
# print(r1)

k = 4
prices = [1,2,4,2,5,7,2,4,9,0]
r1 = sol.maxProfit2(k, prices)
print(r1)
# %%
