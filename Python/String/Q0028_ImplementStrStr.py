# 
# * 28. Implement strStr()
# * Easy

# * Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle 
# is not part of haystack.

# Clarification:

# What should we return when needle is an empty string? This is a great question 
# to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. 
# This is consistent to C's strstr() and Java's indexOf().

 
# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Example 3:
# Input: haystack = "", needle = ""
# Output: 0

# Constraints:
#     0 <= haystack.length, needle.length <= 5 * 104
#     haystack and needle consist of only lower-case English characters.

#%%

class Solution:
    # * Solution 1
    def strStr1(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(n-m+1):
            if haystack[i:i+m] == needle:
                return i
        
        return -1



sol = Solution()
a1 = 'hello'
a2 = 'll'
r1 = sol.strStr1(a1, a2)
print(r1)

a1 = 'aaaaa'
a2 = 'bba'
r1 = sol.strStr1(a1, a2)
print(r1)

a1 = ''
a2 = ''
r1 = sol.strStr1(a1, a2)
print(r1)

a1 = 'a'
a2 = 'a'
r1 = sol.strStr1(a1, a2)
print(r1)

a1 = 'abc'
a2 = 'c'
r1 = sol.strStr1(a1, a2)
print(r1)
# %%
