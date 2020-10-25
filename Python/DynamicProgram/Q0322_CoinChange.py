#
# * 322. Coin Change
# * Medium

# * You are given coins of different denominations and a total amount of money 
# * amount. Write a function to compute the fewest number of coins that you need 
# * to make up that amount. If that amount of money cannot be made up by any 
# * combination of the coins, return -1.

# * You may assume that you have an infinite number of each kind of coin.

# * Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# * Example 2:

# Input: coins = [2], amount = 3
# Output: -1

# * Example 3:

# Input: coins = [1], amount = 0
# Output: 0

# * Example 4:

# Input: coins = [1], amount = 1
# Output: 1

# * Example 5:

# Input: coins = [1], amount = 2
# Output: 2

# * Constraints:

#     1 <= coins.length <= 12
#     1 <= coins[i] <= 231 - 1
#     0 <= amount <= 104

#%%
class Solution:

    # * Solution 1
    # ! Brute force
    def coinChange1(self, coins: list, amount: int) -> int:
        
        def dp(n:int):
            if n == 0:
                return 0
            if n < 0:
                return -1

            result = float('inf')

            for coin in coins:
                subResult = dp(n -coin)
                if subResult < 0:
                    continue
                result = min(result, 1 + subResult)

            return result if result != float('inf') else -1

        return dp(amount)
        

    # * Solution 2
    # ! with a memo
    def coinChange2(self, coins: list, amount: int) -> int:
        memo = dict()

        def dp(n:int):
            if n in memo: 
                return memo[n]
            
            if n == 0:
                return 0
            if n < 0:
                return -1

            result = float('inf')

            for coin in coins:
                subResult = dp(n -coin)
                if subResult < 0:
                    continue
                result = min(result, 1 + subResult)
            
            memo[n] = result if result != float('inf') else -1

            return memo[n]

        return dp(amount)


    # * Solution 3
    # ! from bottom up
    def coinChange3(self, coins: list, amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0

        for i in range(amount+1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i-coin])

        return -1 if dp[amount] == amount + 1 else dp[amount]
        


sol = Solution()
a1 = [1, 2, 5]
a2 = 11
r1 = sol.coinChange1(a1, a2)
print(r1)


# %%
