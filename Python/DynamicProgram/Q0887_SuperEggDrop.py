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

    
    # * Solution 3
    # ! Recurisve with memo, plus binary search
    def superEggDrop3(self, K: int, N: int) -> int:
        memo = {}

        def dp(K:int, N:int) -> int:
            if K == 1:
                return N
            if N == 0:
                return 0
            if (K, N) in memo:
                return memo[(K, N)]

            result = float('INF')
            # ? old implementation in solution 2
            # for i in range(1, N+1):
            #     result = min(result, max(dp(K, N-i), dp(K-1, i-1))+1)
            # ! new binary search
            low = 1
            high = N
            while low <= high:
                middle = (low + high)//2
                broken = dp(K - 1, middle - 1) # 碎
                not_broken = dp(K, N - middle) # 没碎
                # res = min(max(碎，没碎) + 1)
                if broken > not_broken:
                    high = middle - 1
                    result = min(result, broken + 1)
                else:
                    low = middle + 1
                    result = min(result, not_broken + 1)

            memo[(K, N)] = result
            return result


        return dp(K, N)


    # * Solution 4
    # ! Dynamic with different thought
    def superEggDrop4(self, K: int, N: int) -> int:

        dp = [[0]*(N+1) for _ in range(K+1)]

        # print(dp)
        # dp[1][0] = 99
        # print(dp)

        # * base case: no need, all set in initialization
        # dp[0][..] = 0
        # dp[..][0] = 0

        m = 0
        while(dp[K][m] < N):
            m += 1
            for k in range(1, K+1):
                dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1;

        return m


    # * Solution 5
    # ! Dynamic Programming with Optimality Criterion, From solutions
    def superEggDrop5(self, K, N):

        #  * Right now, dp[i] represents dp(1, i)
        dp = list(range(N+1))

        for k in range(2, K+1):
            # * Now, we will develop dp2[i] = dp(k, i)
            dp2 = [0]
            x = 1
            for n in range(1, N+1):
                # * Let's find dp2[n] = dp(k, n)
                # * Increase our optimal x while we can make our answer better.
                # * Notice max(dp[x-1], dp2[n-x]) > max(dp[x], dp2[n-x-1])
                # * is simply max(T1(x-1), T2(x-1)) > max(T1(x), T2(x)).
                while x < n and max(dp[x-1], dp2[n-x]) > max(dp[x], dp2[n-x-1]):
                    x += 1

                # * The final answer happens at this x.
                dp2.append(1 + max(dp[x-1], dp2[n-x]))

            dp = dp2

        return dp[-1]    


    # * Solution 6
    # ! Classic Dynamic programming
    # ! TLE
    def superEggDropDrop(self, K, N):

        # * classic dp[K+1][N+1]
        # * initialized with positive Infinity
        dp = [[float('inf')] * (N+1) for _ in range(K+1)]

        # * fill with base case
        # * 1) To verify 0 floor, need drop 0 time.
        # * 2) To verify 1 floor, need drop 1 time.
        for k in range(1, K+1):
            dp[k][0] = 0
            dp[k][1] = 1
        # * 3) Only 1 egg left, to verify n floor, need drop n times.
        for n in range(1, N+1):
            dp[1][n] = n

        for i in range(2, K+1):
            for j in range(2, N+1):
                for k in range(1, j+1):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][k-1], dp[i][j-k]))
        
        return dp[K][N]
        


sol = Solution()
k1 = 1
n1 = 2
r1 = sol.superEggDrop5(k1, n1)
print('ex: {}, res: {}'.format(2, r1))

k1 = 2
n1 = 6
r1 = sol.superEggDrop5(k1, n1)
print('ex: {}, res: {}'.format(3, r1))

k1 = 3
n1 = 14
r1 = sol.superEggDrop5(k1, n1)
print('ex: {}, res: {}'.format(4, r1))

k1 = 3
n1 = 25
r1 = sol.superEggDrop5(k1, n1)
print('ex: {}, res: {}'.format(5, r1))

k1 = 4
n1 = 2000
r1 = sol.superEggDrop5(k1, n1)
print('ex: {}, res: {}'.format(16, r1))
# %%
