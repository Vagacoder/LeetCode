#
# * 76. Minimum Window Substring
# ! Hard

# * Given two strings s and t, return the minimum window in s which will contain 
# * all the characters in t. If there is no such window in s that covers all 
# * characters in t, return the empty string "".

# * Note that If there is such a window, it is guaranteed that there will always 
# * be only one unique minimum window in s.

 

# * Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"

# * Example 2:

# Input: s = "a", t = "a"
# Output: "a"

# * Constraints:

#     1 <= s.length, t.length <= 105
#     s and t consist of English letters.
 
# ! Follow up: Could you find an algorithm that runs in O(n) time?

#%%

class Solution:

    # * Solution 1
    # * Brutal force, time limits exceeded
    def minWindow1(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        # print('n:',n)
        # print('m:',m)

        dictT = {}
        for c in t:
            if c in dictT:
                dictT[c] +=1
            else:
                dictT[c] = 1
        
        # print(dictT)

        minS = s+'a'
        for i in range(n):

            for j in range(i+m, n+1):
                # print('i: {}, j: {}'.format(i, j))
                subS = s[i:j]

                # print(subS)

                dictSubS = {}
                for c in subS:
                    if c in dictSubS:
                        dictSubS[c] +=1
                    else:
                        dictSubS[c] = 1

                # print(dictSubS)
                
                for c, count in dictT.items():
                    if c not in dictSubS:
                        break
                    elif dictSubS[c] < count:
                        break
                else:
                    if len(subS) < len(minS):
                        minS = subS

        if minS != s+'a':
            return minS
        else:
            return ''


    # * Solution 2 
    # * Sliding window
    def minWindow2(self, s: str, t: str) -> str:

        n = len(s)
        m = len(t)
        # print('n:',n)
        # print('m:',m)

        # * dictT, map(char, frequency) in t
        dictT = {}
        for c in t:
            if c in dictT:
                dictT[c] +=1
            else:
                dictT[c] = 1
        
        # print(dictT)

        # * dictWindow, map(char, frequency) in sliding window
        dictWindow = {}

        # * pointers of left and right bound of window,
        left = 0
        right = 0

        # ! inside window, how many chars whose frequency are equal to t
        valid = 0

        # * minmum covery string
        minS = s+'a'

        while right < n:
            # * newC is the char to be added into window
            newC = s[right]
            # * window right bound moving ahead
            right += 1

            # ! Operations to update window
            # * newly added char in t
            if newC in dictT:
                if newC in dictWindow:
                    dictWindow[newC] += 1
                else:
                    dictWindow[newC] = 1

                if dictWindow[newC] == dictT[newC]:
                    valid +=1
            
            # ! Whether the left bound shrink
            # *  vaild == len(dictT): char in window matching char in t
            while valid == len(dictT):
                if (right - left) < len(minS):
                    minS = s[left:right]

                # * removeC is the char to be removed from window
                removeC = s[left]
                # * window left bound to be shrink
                left += 1

                # ! Operations to update window
                # * newly removing char in t
                if removeC in dictT:
                    if dictWindow[removeC] == dictT[removeC]:
                        valid -= 1
                    dictWindow[removeC] -= 1
        
        # * return 
        if minS != s+'a':
            return minS
        else:
            return ''


sol = Solution()
a1 = 'ADOBECODEBANC'
t1 = 'ABC'
r1 = sol.minWindow2(a1, t1)
print('r1:', r1)

a2 = 'A'
t2 = 'A'
r2 = sol.minWindow2(a2, t2)
print('r2:', r2)

a3 = 'bbaa'
t3 = 'aba'
r3 = sol.minWindow2(a3, t3)
print('r3:', r3)
# %%
