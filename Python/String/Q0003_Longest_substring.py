#
# * 3. Longest Substring Without Repeating Characters
# ! Hard
# * Given a string, find the length of the longest substring without repeating characters.

# * Example 1:
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 

# * Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# * Example 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

#%%

class Solution:
    
    # ? Solution 1. Not working
    def lengthOfLongestSubstring1(self, s: str) -> int:
        lengthOfString = len(s)
        if lengthOfString == 1:
            return 1
        maxLength = 0
        repeat = False
        dic = {}
        lastCalculation = 0

        for i in range(lengthOfString):
            char = s[i]
            if char in dic:
                # find first repeat
                if not repeat:
                    repeat = True
                    maxLength = i
                # not first repeat
                else:
                    currentLength = i - (dic[char] if (dic[char] > lastCalculation ) else lastCalculation)
                    if currentLength > maxLength:
                        maxLength = currentLength
                lastCalculation = i
            # update dict                
            dic[char] = i

        if repeat:
            if (lengthOfString - lastCalculation) < maxLength:
                return maxLength
            else:
                return lengthOfString - lastCalculation
        else:
            return lengthOfString



    # * Solution 2. works but slow O(n^3)
    def lengthOfLongestSubstring2(self, s: str) -> int:
        lengthOfString = len(s)
        maxLength = 0
        for i in range (lengthOfString):
            for j in range(i, lengthOfString):
                subString = s[i:j+1]
                if self.isUnique(subString) and len(subString) > maxLength:
                    maxLength = len(subString)
        
        return maxLength
                    
    def isUnique(self, s:str) -> bool:
        setOfString = set(s)
        return len(setOfString) == len(s)



    # * Solution 3. Works, need improvement
    def lengthOfLongestSubstring3(self, s: str) -> int:
        lengthOfString = len(s)
        cur1 = 0
        cur2 = 0
        maxLength = 0

        while (cur2 <= lengthOfString):
            subString = s[cur1:cur2]
            if self.isUnique(subString):
                cur2 += 1
                if len(subString) > maxLength:
                    maxLength = len(subString)         
            else:
                if (cur1>=cur2):
                    cur2 += 1
                else:
                    cur1 += 1
            
        return maxLength

    def isUnique(self, s:str) -> bool:
        setOfString = set(s)
        return len(setOfString) == len(s)



    # * Solution 4
    def lengthOfLongestSubstring4(self, s: str) -> int:
        n = len(s)

        dictWindow = {}

        left = 0
        right = 0
        maxLength = 0
        while right < n:
            newC = s[right]
            right += 1

            if newC in dictWindow:
                dictWindow[newC] += 1
            else:
                dictWindow[newC] = 1
            
            while dictWindow[newC] > 1:
                removeC = s[left]
                left += 1
                dictWindow[removeC] -= 1
            
            maxLength = max(maxLength, right-left)
        
        return maxLength




input1 = "abcabcbb"
input2 = "bbbbbb"
input3 = "pwwkew"
input4 = ""
input5 = " "
input6 = "au"
input7 = "aab"
input8 = "cdd"
input9 = "abba"
input10 = "dvdf"

sol = Solution()
print("abcabcbb should 3, mine is: ", sol.lengthOfLongestSubstring4(input1))
print("bbbbbb should 1, mine is: " , sol.lengthOfLongestSubstring4(input2))
print("pwwkew should 3, mine is: " , sol.lengthOfLongestSubstring4(input3))
print("empty should 0, mine is: " , sol.lengthOfLongestSubstring4(input4))
print("space should 1, mine is: " , sol.lengthOfLongestSubstring4(input5))
print("au should 2, mine is: " , sol.lengthOfLongestSubstring4(input6))
print("aab should 2, mine is: " , sol.lengthOfLongestSubstring4(input7))
print("cdd should 2, mine is: " , sol.lengthOfLongestSubstring4(input8))
print("abba should 2, mine is: " , sol.lengthOfLongestSubstring4(input9))
print("dvdf should 3, mine is: " , sol.lengthOfLongestSubstring4(input10))

# %%
