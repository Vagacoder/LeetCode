#
# * 877. Stone Game
# * Medium

# * Alex and Lee play a game with piles of stones.  There are an even number of 
# * piles arranged in a row, and each pile has a positive integer number of stones 
# * piles[i].

# The objective of the game is to end with the most stones.  The total number of 
# stones is odd, so there are no ties.

# Alex and Lee take turns, with Alex starting first.  Each turn, a player takes 
# the entire pile of stones from either the beginning or the end of the row.  
# This continues until there are no more piles left, at which point the person 
# with the most stones wins.

# Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

 
# * Example 1:

# Input: piles = [5,3,4,5]
# Output: true

# Explanation: 
# Alex starts first, and can only take the first 5 or the last 5.
# Say he takes the first 5, so that the row becomes [3, 4, 5].
# If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
# If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alex, so we return true.

 

# * Constraints:

#     2 <= piles.length <= 500
#     piles.length is even.
#     1 <= piles[i] <= 500
#     sum(piles) is odd.

#%%

class Solution:

    # * Solution 1
    # ! passed, but could have potential bug, see below
    def stoneGame(self, piles: list) -> bool:
        n = len(piles)
        dp = [[-1] * n for _ in range(n)]

        # * base case
        # for i in range(n-1):
        #     dp[i][i+1] = max(piles[i], piles[i+1])

        print(dp)
        
        def helper(start: int, end: int)-> int:
            # * read memo
            if dp[start][end] != -1:
                return dp[start][end]
            
            # * base case
            if start+1 == end:
                dp[start][end] = max(piles[start], piles[end])
                return dp[start][end]
            
            # ! potenital bug, since we pick start (end), we assume opponent pick other side
            dp[start][end] = max((piles[start] + helper(start+1, end-1)), (piles[end] + helper(start+1,end-1)))
            return dp[start][end]
        
        alexGet = helper(0, n-1)
        # print(alexGet)
        # print(sum(piles))
        # print(dp)
        return alexGet > sum(piles) - alexGet
            

    # * Solution 2
    # ! derived from 1, try to fix bug
    # ! passed, feel better LOL
    def stoneGame2(self, piles: list) -> bool:
        n = len(piles)
        dp = [[-1] * n for _ in range(n)]
        
        def helper(start: int, end: int)-> int:
            # * read memo
            if dp[start][end] != -1:
                return dp[start][end]
            
            # * base case
            if start+1 == end:
                dp[start][end] = max(piles[start], piles[end])
                return dp[start][end]
            
            # ! fix bug
            dp[start][end] = max(
                (piles[start] + max(helper(start+1, end-1), helper(start+2, end))), 
                (piles[end] + max(helper(start+1,end-1), helper(start,end-2)))
                )
            return dp[start][end]
        
        alexGet = helper(0, n-1)
        return alexGet > sum(piles) - alexGet

    
    # * Solution 3
    def stoneGame3(self, piles:list) -> bool:
        n = len(piles)

        # * Initialize dp
        dp =[[(0,0)] * n for _ in range(n)]

        # * base case
        for i in range(n):
            dp[i][i] = (piles[i], 0)

        print(dp)

        for j in range(1, n):
            for i in range(j-1, -1, -1):
    
                # print('i', i)
                # print('j', j)
                # print()

                # * first one pick left
                left = piles[i] + dp[i+1][j][1]
                # * first one pick right
                right = piles[j] + dp[i][j-1][1]

                if left > right:
                    dp[i][j] = (left, dp[i+1][j][0])
                else:
                    dp[i][j] = (right, dp[i][j-1][0])

        print(dp)
                    
        return dp[0][n-1][0] > dp[0][n-1][1]

sol = Solution()
a1 = [5, 3, 4, 5]
r1 = sol.stoneGame3(a1)
print(r1)

a1 = [3, 7, 2, 3]
r1 = sol.stoneGame3(a1)
print(r1)
