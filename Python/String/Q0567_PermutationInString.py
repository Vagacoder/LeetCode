#
# * 567. Permutation in Strnig
# * Medium

# * Given two strings s1 and s2, write a function to return true if s2 contains 
# * the permutation of s1. In other words, one of the first string's permutations 
# * is the substring of the second string.

 

# * Example 1:

# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").

# * Example 2:

# Input:s1= "ab" s2 = "eidboaoo"
# Output: False

 

# * Constraints:

#     The input strings only contain lower case letters.
#     The length of both given strings is in range [1, 10,000].

#%%

class Solution:

    # * Solution 1
    # * Sliding window, by myself
    def checkInclusion1(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        # print('n1', n1)
        # print('n2', n2)

        dict1 = {}
        for c in s1:
            if c in dict1:
                dict1[c] +=1
            else:
                dict1[c] =1

        sizeDict1 = len(dict1)

        # print(dict1)

        # for key in dict1.keys():
        #     print(key)

        dictWindow = {}

        left = 0
        right = n1-1
        valid = 0

        for c in s2[left:right]:
            if c in dict1:
                if c in dictWindow:
                    dictWindow[c] +=1
                else:
                    dictWindow[c] = 1
                
                if dictWindow[c] == dict1[c]:
                    valid += 1
        
        # print(dictWindow)
        # print(valid)

        while right < n2:
            newC = s2[right]
            right += 1

            if newC in dict1:

                # print('newC in dict1')

                if newC in dictWindow:
                    dictWindow[newC] +=1
                else:
                    dictWindow[newC] = 1

                if dictWindow[newC] == dict1[newC]:

                    # print('updating valis', valid)

                    valid += 1
                    
                    # print('updated valid', valid)

                
                if valid == sizeDict1:
                    return True

            removeC = s2[left]
            left += 1

            if removeC in dict1:
                if removeC in dictWindow:
                    if dictWindow[removeC] == dict1[removeC]:
                        valid -= 1
                    dictWindow[removeC] -=1


        return False
            

    # * Solution 2
    # * From tutorail
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        # print('n1', n1)
        # print('n2', n2)

        dict1 = {}
        for c in s1:
            if c in dict1:
                dict1[c] +=1
            else:
                dict1[c] =1

        sizeDict1 = len(dict1)

        dictWindow = {}

        left = 0
        right = 0
        valid = 0

        while right < n2:
            newC = s2[right]
            right += 1
            if newC in dict1:
                if newC in dictWindow:
                    dictWindow[newC] +=1
                else:
                    dictWindow[newC] = 1
                if dictWindow[newC] == dict1[newC]:
                    valid += 1

            while right - left >= n1:
                if valid == sizeDict1:
                    return True

                removeC = s2[left]
                left += 1

                if removeC in dict1 and removeC in dictWindow:
                    if dictWindow[removeC] == dict1[removeC]:
                       valid -= 1
                    dictWindow[removeC] -= 1

        return False


sol = Solution()

s1 = 'ab'
s2 = 'eidbaooo'
r1 = sol.checkInclusion2(s1, s2)
print(r1)

s1 = 'ab'
s2 = 'eidboaoo'
r1 = sol.checkInclusion2(s1, s2)
print(r1)

s1 = 'abcdxabcde'
s2 = 'abcdeabcdx'
r1 = sol.checkInclusion2(s1, s2)
print(r1)

# %%
