#
# * 72. Edit Distance
# ! Hard

# * Given two strings word1 and word2, return the minimum number of operations 
# * required to convert word1 to word2.

# * You have the following three operations permitted on a word:

#     Insert a character
#     Delete a character
#     Replace a character

 

# * Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

# * Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

 

# * Constraints:

#     0 <= word1.length, word2.length <= 500
#     word1 and word2 consist of lowercase English letters.

#%%

class Solution:

    # * Solution 1
    # * from End to Beginning
    def minDistance1(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        memo = {}

        def dp(i, j):
            if i == -1:
                return j+1
            if j == -1:
                return i+1
            if (i, j) in memo:
                return memo[(i, j)]
            
            if word1[i] == word2[j]:
                memo[(i,j)] =  dp(i-1, j-1)
            else:
                memo[(i,j)] = min(dp(i, j-1)+1, dp(i-1, j)+1, dp(i-1,j-1)+1)

            return memo[(i,j)]
        
        return dp(n-1, m-1)


    # * Solution 2
    # * from Beginning to End
    def minDistance2(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        memo = {}

        def dp(i, j):
            if i >= n:
                return m - j
            if j >= m:
                return n - i
            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                memo[(i,j)] =  dp(i+1, j+1)
            else:
                memo[(i,j)] =  min(dp(i, j+1)+1, dp(i+1, j)+1, dp(i+1, j+1)+1)
            
            return memo[(i,j)]

        return dp(0,0)



sol = Solution()
w1 = 'horse'
w2 = 'ros'
r1 = sol.minDistance2(w1, w2)
print(r1)

w1 = 'intention'
w2 = 'execution'
r1 = sol.minDistance2(w1, w2)
print(r1)

w1 = 'dinitrophenylhydrazine'
w2 = 'benzalphenylhydrazone'
r1 = sol.minDistance2(w1, w2)
print(r1)
