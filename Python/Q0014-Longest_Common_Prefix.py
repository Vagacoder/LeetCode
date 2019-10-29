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
        if (strs == None or len(strs) == 0): return ""
        result = strs[0]

        for i in range(1, len(strs)):
            while (not (strs[i].startswith(result))):
                result = result[0: len(result)-1]
                if (result == ""):
                    return result
        
        return result


# Solution 3 Vertical scanning
class Solution3:
    def longestCommonPrefix(self, strs: [str]) -> str:
        result = ""
        if (strs == None or len(strs) == 0):
            return result
        
        for i in range(0, len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if (i == len(strs[j]) or strs[j][i] != c):
                    return strs[0][0:i]

        return strs[0]

# Solution 4 Divide and conquer
class Solution4:
    def longestCommonPrefix(self, strs: [str]) -> str:
        result = ""
        if (strs == None or len(strs) == 0):
            return result
        return self.findLongestCommonPrefix(strs, 0, len(strs) -1)

    def findLongestCommonPrefix(self, strs: [str], l: int, r: int) -> str:
        if (l == r) :
            return strs[l]
        else:
            mid = (l+r)//2
            lcpLeft = self.findLongestCommonPrefix(strs, l, mid)
            lcpRight = self.findLongestCommonPrefix(strs, mid+1, r);
            return self.commonPrefix(lcpLeft, lcpRight)

    def commonPrefix(self, left: str, right: str)->str:
        minLen = min(len(left), len(right))
        for i in range(0, minLen):
            if (left[i] != right[i]):
                return left[0:i]
        return left[0: minLen]

# Solution 5 binary search
class Solution5:
    def longestCommonPrefix(self, strs:[str]) -> str:
        result = ""
        if (strs == None or len(strs) == 0):
            return result
        minLen : int = len(strs[0])
        for str in strs:
            minLen = min(minLen, len(str));
        low = 1;
        high = minLen
        while (low <= high):
            mid = (low + high) // 2
            if (self.isCommonPrefix(strs, mid)):
                low = mid + 1
            else:
                high = mid - 1
        return strs[0][0: (low + high)//2]

    def isCommonPrefix(self, s: [str], length: int) -> bool:
        str1 = s[0][0: length]
        for j in range(1, len(s)):
            if (not s[j].startswith(str1)):
                return False
        return True


sol=Solution5()
print('Input is ["flower","flow","flight"], expect: "fl", mine is: ',sol.longestCommonPrefix(['flower', 'flow', 'flight']));
print('Input is ["c","c","c"], expect: "c", mine is: ',sol.longestCommonPrefix(['c', 'c', 'c']));
print('Input is ["dog","racecar","car"], expect: "", mine is: ',sol.longestCommonPrefix(["dog","racecar","car"]));
print('Input is ["c","acc","ccc"], expect: "", mine is: ',sol.longestCommonPrefix(["c","acc","ccc"]));
