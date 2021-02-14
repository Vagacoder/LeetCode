#
# * 651. 4 Keys Keyboard
# * Medium
# ! Locked

# * Imagine you have a special keyboard with the following keys: 
# Key 1:  Prints 'A' on screen
# Key 2: (Ctrl-A): Select screen
# Key 3: (Ctrl-C): Copy selection to buffer
# Key 4: (Ctrl-V): Print buffer on screen appending it
#                  after what has already been printed. 

# If you can only press the keyboard for N times (with the above four
# keys), write a program to produce maximum numbers of A's. That is to
# say, the input parameter is N (No. of keys that you can press), the 
# output is M (No. of As that you can produce).

# * Examples:

# Input:  N = 3
# Output: 3
# We can at most get 3 A's on screen by pressing 
# following key sequence.
# A, A, A

# Input:  N = 7
# Output: 9
# We can at most get 9 A's on screen by pressing 
# following key sequence.
# A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V

# Input:  N = 11
# Output: 27
# We can at most get 27 A's on screen by pressing 
# following key sequence.
# A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V, Ctrl A, 
# Ctrl C, Ctrl V, Ctrl V

#%%

class Solution:

    # * Solution 1
    # ! Recursive
    def maxA1(self, N:int) -> int:
        
        # * recursive helper
        def dp(strikes:int, ANumber: int, copiedA: int):
            # * base case
            if strikes <= 0:
                return ANumber
            
            return max(
                        dp(strikes-1, ANumber + 1, copiedA),
                        dp(strikes-1, ANumber + copiedA, copiedA),
                        dp(strikes-2, ANumber, ANumber)
                        )

        return dp(N, 0, 0)


    # * Solution 2
    # ! Recursive with memo
    def maxA2(self, N:int) -> int:

        memo = {}

        # * recursive helper
        def dp(strikes:int, ANumber: int, copiedA: int):
            # * base case
            if strikes <= 0:
                return ANumber

            if (strikes, ANumber, copiedA) in memo:
                return memo[(strikes, ANumber, copiedA)]
            
            result = max(
                        dp(strikes-1, ANumber + 1, copiedA),
                        dp(strikes-1, ANumber + copiedA, copiedA),
                        dp(strikes-2, ANumber, ANumber)
                        )

            memo[(strikes, ANumber, copiedA)] = result
            return result

        return dp(N, 0, 0)


    # * Solution 3
    # ! Dynamic Programm
    def maxA3(self, N:int) -> int:

        if N <= 0:
            return 0
        if N == 1:
            return 1

        # * dp table
        # ? dp[i][0]: A number on screen
        # ? dp[i][1]: copid A number
        dp = [(0, 0) for _ in range(N+1)]

        # * base case
        dp[1] = (1, 0)

        for i in range(2, N):
            dp[i] = max(
                        dp[i-1]
                        )


sol = Solution()

a1 = 3
r1 = sol.maxA2(a1)
print('ex: {}, ar: {}'.format(3, r1))

a1 = 7
r1 = sol.maxA2(a1)
print('ex: {}, ar: {}'.format(9, r1))

a1 = 11
r1 = sol.maxA2(a1)
print('ex: {}, ar: {}'.format(27, r1))
