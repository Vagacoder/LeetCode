#
# * 516. Longest Palindromic Subsequence
# * Medium

# * Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

# * Example 1:
# Input: "bbbab"
# Output: 4

# One possible longest palindromic subsequence is "bbbb".

 
# * Example 2:
# Input: "cbbd"
# Output: 2

# One possible longest palindromic subsequence is "bb".


# * Constraints:

#     1 <= s.length <= 1000
#     s consists only of lowercase English letters.

#%%
class Solution:

    # * Solution 1
    # ! Dynamic programming
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        # * initial dp[n][n]
        dp = [[0] * n for _ in range(n)]

        # * two pointers, i: start, j: end
        # * base case, i = j, string length = 1, its palidrome whose length = 1
        # for i in range(n):
        #     dp[i][i] = 1

        for i in range(n-1,-1,-1):
            for j in range(i, n):
                # * here is base cases
                if i == j:
                    dp[i][j] = 1

                else:
                    # * state transfer functions
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        return dp[0][n-1]


    # * Solution 2
    # ! Recursive with memo
    def longestPalindromeSubseq2(self, s: str) -> int:
        
        memo = {}

        def helper(s: str, i:int, j:int) -> int:
            # * check memo
            if (i,j) in memo:
                return memo[(i,j)]
            # * base case
            if i > j:
                return 0
            if i == j:
                return 1
            
            if s[i] == s[j]:
                memo[(i,j)] = helper(s, i+1, j-1) + 2
            else:
                memo[(i,j)] = max(helper(s, i, j-1), helper(s, i+1, j))

            return memo[(i,j)]
        

        return helper(s, 0, len(s)-1)


sol = Solution()
a1 = 'abdfcab'
r1 = sol.longestPalindromeSubseq2(a1)
print(r1)

a1 = 'bbbab'
r1 = sol.longestPalindromeSubseq2(a1)
print(r1)

a1 = 'cbbd'
r1 = sol.longestPalindromeSubseq2(a1)
print(r1)
