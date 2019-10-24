# 14. Longest Common Prefix
# Easy
# Write a function to find the longest common prefix string amongst an array of
# strings. If there is no common prefix, return an empty string "".

# Example 1:
# Input: ['flower', 'flow', 'flight']
# Output: 'fl'

# Example 2:
# Input: ['dog', 'racecar', 'car']
# Output: ''
# Explain: there is no common prefix among the input strings.

# Note:
# All given inputs are in lowercase letters a-z

# Solution 1
class Solution1:
    def longestCommonPrefix(self, strs: [str]) -> str:
        result = ""
        lengthOfStrs = len(strs)
        if (lengthOfStrs == 0):
            return result
        elif (lengthOfStrs == 1):
            return strs[0]
        else:
            lengthOfFirstStr = len(strs[0])
            isGoodPrefix = True
            for i in range(0, lengthOfFirstStr):
                currentPrefix = strs[0][0:(i+1)]
                print(currentPrefix)
                for j in range(1, lengthOfStrs):
                    if (not strs[j].startswith(currentPrefix)):
                        isGoodPrefix = False
                        break
                if (isGoodPrefix):
                    result = currentPrefix
                else:
                    break

        return result

# Solution 2, horizontal scanning, 
class Solution2:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if (len(strs) == 0): return ""
        result = strs[0]

        for i in range(1, len(strs)):
            while (not (strs[i].startswith(result))):
                result = result[0: len(result)-1]
                if (result == ""):
                    return result
        
        return result



sol=Solution2()
print('Input is ["flower","flow","flight"], expect: "fl", mine is: ',sol.longestCommonPrefix(['flower', 'flow', 'flight']));
print('Input is ["c","c","c"], expect: "c", mine is: ',sol.longestCommonPrefix(['c', 'c', 'c']));
print('Input is ["dog","racecar","car"], expect: "", mine is: ',sol.longestCommonPrefix(["dog","racecar","car"]));
print('Input is ["c","acc","ccc"], expect: "", mine is: ',sol.longestCommonPrefix(["c","acc","ccc"]));
