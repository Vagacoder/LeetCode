#
# * 509, Fibonacci Number
# * The Fibonacci numbers, commonly denoted F(n) form a sequence, called the 
# * Fibonacci sequence, such that each number is the sum of the two preceding 
# * ones, starting from 0 and 1. That is,

# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.

# Given N, calculate F(N).

 

# * Example 1:

# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# * Example 2:

# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# * Example 3:

# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


#%%

class Solution:

    # * Solution 1
    # ! Simple recursive
    def fib1(self, N:int)->int:
        if N == 0 or N ==1:
            return N

        return self.fib(N-1) + self.fib(N-2)


    # * Solution 2
    # ! Recursive with memo
    def fib2(self, N:int)->int:
        if N == 0 or N ==1:
            return N

        memo = [-1]*(N+1)
        memo[0] = 0
        memo[1] = 1

        # * Helper
        def fib2Recursive(memo:list, N:int):
            if memo[N] != -1:
                return memo[N]
            
            memo[N] = fib2Recursive(memo, N-1) + fib2Recursive(memo, N-2)
            return memo[N]


        return fib2Recursive(memo, N)

            
    # * Solution 3
    # ! Dynamic Programming
    def fib3(self, N:int)->int:
        if N == 0 or N == 1:
            return N

        dp = [0] * (N+1)
        dp[1] = dp[2] = 1
        for i in range(3, N+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[N]




sol1 = Solution()
n1 = 5
e1 = 5
r1 = sol1.fib2(n1)
print('For {}, Expected: {}, Result: {}'.format(n1, e1, r1))

n1 = 3
e1 = 2
r1 = sol1.fib2(n1)
print('For {}, Expected: {}, Result: {}'.format(n1, e1, r1))

# %%
