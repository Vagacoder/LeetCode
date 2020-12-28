#
# * 887. Super Egg Drop
# ! Hard

# * You are given K eggs, and you have access to a building with N floors from 1 to N. 

# * Each egg is identical in function, and if an egg breaks, you cannot drop it 
# * again.

# * You know that there exists a floor F with 0 <= F <= N such that any egg dropped 
# * at a floor higher than F will break, and any egg dropped at or below floor F 
# * will not break.

# Each move, you may take an egg (if you have an unbroken one) and drop it from 
# any floor X (with 1 <= X <= N). 

# Your goal is to know with certainty what the value of F is.

# What is the minimum number of moves that you need to know with certainty what 
# F is, regardless of the initial value of F?

# * Example 1:
# Input: K = 1, N = 2
# Output: 2

# ? Explanation: 
# Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
# Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
# If it didn't break, then we know with certainty F = 2.
# Hence, we needed 2 moves in the worst case to know what F is with certainty.

# * Example 2:
# Input: K = 2, N = 6
# Output: 3

# * Example 3:
# Input: K = 3, N = 14
# Output: 4

# * Note:
#     1 <= K <= 100
#     1 <= N <= 10000

#%%

class Solution:

    # * Solution 1
    # ! Recursive, TLE
    def superEggDrop(self, K: int, N: int) -> int:
        if K == 1:
            return N
        if N == 0:
            return 0

        result = float('INF')
        for i in range(1, N+1):
            result = min(result, max(self.superEggDrop(K, N-i), self.superEggDrop(K-1, i-1))+1)

        return result

    # * Solution 2
    # ! Recursive with memo
    # ! Still TLE
    def superEggDrop2(self, K: int, N: int) -> int:

        memo = {}

        def dp(K:int, N:int) -> int:
            if K == 1:
                return N
            if N == 0:
                return 0
            if (K, N) in memo:
                return memo[(K, N)]

            result = float('INF')
            for i in range(1, N+1):
                result = min(result, max(dp(K, N-i), dp(K-1, i-1))+1)

            memo[(K, N)] = result
            return result


        return dp(K, N)
    

sol = Solution()
k1 = 1
n1 = 2
r1 = sol.superEggDrop2(k1, n1)
print('ex: {}, res: {}'.format(2, r1))

k1 = 2
n1 = 6
r1 = sol.superEggDrop2(k1, n1)
print('ex: {}, res: {}'.format(3, r1))

k1 = 3
n1 = 14
r1 = sol.superEggDrop2(k1, n1)
print('ex: {}, res: {}'.format(4, r1))

k1 = 3
n1 = 25
r1 = sol.superEggDrop2(k1, n1)
print('ex: {}, res: {}'.format(5, r1))

k1 = 4
n1 = 2000
r1 = sol.superEggDrop2(k1, n1)
print(r1)
# %%
