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
            
            dp[start][end] = max((piles[start] + helper(start+1, end-1)), (piles[end]) + helper(start+1,end-1))
            return dp[start][end]
        
        alexGet = helper(0, n-1)
        # print(alexGet)
        # print(sum(piles))
        # print(dp)
        return alexGet > sum(piles) - alexGet
            



sol = Solution()
a1 = [5, 3, 4, 5]
r1 = sol.stoneGame(a1)
print(r1)

a1 = [5, 3, 4, 5]
r1 = sol.stoneGame(a1)
print(r1)
