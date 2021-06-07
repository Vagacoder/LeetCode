# 
# * 10. Regular Expression Matching
# ! Hard

# * Given an input string (s) and a pattern (p), implement regular expression 
# * matching with support for '.' and '*' where: 

#     '.' Matches any single character.​​​​
#     '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# * Example 1:
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# * Example 2:
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# * Example 3:
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

# * Example 4:
# Input: s = "aab", p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

# * Example 5:
# Input: s = "mississippi", p = "mis*is*p*."
# Output: false

# * Constraints:
#     0 <= s.length <= 20
#     0 <= p.length <= 30
#     s contains only lowercase English letters.
#     p contains only lowercase English letters, '.', and '*'.
#     It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

#%%

class Solution:

    # * Solution 1
    # ! Most works, not working for 'a*a', may be iterate from the end will work
    def isMatch(self, s: str, p: str) -> bool:
        sCur = 0
        pCur = 0
        sN = len(s)
        pN = len(p)
        while sCur < sN and pCur < pN:
            if p[pCur] == '.':
                if pCur < pN-1 and p[pCur+1] == '*':
                    sCur += 1
                else:
                    sCur += 1
                    pCur += 1
            elif p[pCur] == s[sCur]:
                if pCur < pN-1 and p[pCur+1] == '*':
                    sCur += 1
                else:
                    sCur += 1
                    pCur += 1
            else:
                if pCur < pN-1 and p[pCur+1] == '*':
                    # sCur += 1
                    pCur += 2
                else:
                    sCur += 1
                    pCur = 0

        if pCur < pN-1 and p[pCur+1] == '*':
            pCur += 2

        if pCur == pN and sCur == sN:
            return True
        # elif pCur == pN-2 and p[pCur+1] == '*':
        #     return True
        else:
            return False



    # * Solution 2
    # ! Recursive
    def isMatch2(self, s: str, p: str) -> bool:
        memo = {}

        #  dp 函数
        def dp(s: str, i: int, p: str, j: int) -> bool:
            # base case
            if i == len(s):
                # 如果能匹配空串，一定是字符和 * 成对出现
                if (len(p)-j) % 2 == 1:
                    return False
                # 检查是否为 x*y*z* 这种形式
                for k in range(j, len(p), 2):
                    if p[k+1] != '*':
                        return False
                return True
            
            if j == len(p):
                return i == len(s)
        
            # 检查 memo
            if (i, j) in memo:
                return memo[i, j]

            result = False
            # 匹配
            if s[i] == p[j] or p[j] == '.':
                # 通配符匹配 0 次或多次
                if j < len(p)-1 and p[j+1] == '*':    
                    result = dp(s, i, p, j+2) or dp(s, i+1, p, j)
                # 常规匹配 1 次
                else:    
                    result = dp(s, i+1, p, j+1)
            # 不匹配
            else:
                # 通配符匹配 0 次
                if j < len(p)-1 and p[j+1] == '*':    
                    result = dp(s, i, p, j+2)
                else:
                    result = False

            memo[(i, j)] = result

            return result

        return dp(s, 0, p, 0)



sol = Solution()


s1 = 'aa'
p1 = '..'
r1 = sol.isMatch2(s1, p1)
print('ex: {}, ar: {}'.format(True, r1))

s1 = 'aab'
p1 = 'a.b'
r1 = sol.isMatch2(s1, p1)
print('ex: {}, ar: {}'.format(True, r1))

s1 = 'aa'
p1 = 'a'
r1 = sol.isMatch2(s1, p1)
print('ex: {}, ar: {}'.format(False, r1))

s1 = 'aa'
p1 = 'a*'
r1 = sol.isMatch2(s1, p1)
print('ex: {}, ar: {}'.format(True, r1))

s1 = 'ab'
p1 = '.*'
r1 = sol.isMatch2(s1, p1)
print('ex: {}, ar: {}'.format(True, r1))

s1 = 'aab'
p1 = 'c*a*b'
r1 = sol.isMatch2(s1, p1)
print('ex: {}, ar: {}'.format(True, r1))

s1 = 'mississippi'
p1 = 'mis*is*p*.'
r1 = sol.isMatch2(s1, p1)
print('ex: {}, ar: {}'.format(False, r1))

s1 = 'aaa'
p1 = 'a*a'
r1 = sol.isMatch2(s1, p1)
print('ex: {}, ar: {}'.format(True, r1))

s1 = 'ab'
p1 = '.*c'
r1 = sol.isMatch2(s1, p1)
print('ex: {}, ar: {}'.format(False, r1))
