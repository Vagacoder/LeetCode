#
# * 438. Find All Anagrams in a String
# * Medium

# * Given a string s and a non-empty string p, find all the start indices of p's 
# * anagrams in s.

# * Strings consists of lowercase English letters only and the length of both 
# * strings s and p will not be larger than 20,100.

# * The order of output does not matter.

# * Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# * Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

#%%
class Solution:

    # * Solution 1
    def findAnagrams1(self, s: str, p: str) -> list:
        n1 = len(s)
        n2 = len(p)

        dictP = {}
        for c in p:
            if c in dictP:
                dictP[c] += 1
            else:
                dictP[c] = 1

        sizeDictP = len(dictP)

        # print(dictP)

        dictWindow = {}
        left = 0
        right = 0
        valid = 0
        result = []

        while right < n1:
            newC = s[right]
            right += 1

            if newC in dictP:
                if newC in dictWindow:
                    dictWindow[newC] += 1
                else:
                    dictWindow[newC] = 1
                if dictWindow[newC] == dictP[newC]:
                    valid += 1

            while right - left >= n2:
                if valid == sizeDictP:
                    result.append(left)
                
                removeC = s[left]
                left += 1

                if removeC in dictP and removeC in dictWindow:
                    if dictWindow[removeC] == dictP[removeC]:
                        valid -= 1
                    dictWindow[removeC] -= 1
            
        return result


sol = Solution()
a = 'cbaebabacd'
b = 'abc'
r1 = sol.findAnagrams1(a, b)
print(r1)

# %%
