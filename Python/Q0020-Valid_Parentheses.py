# 20. Valid Parentheses
# Easy

# Given a string containnig just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:
#   1. Open brackets must be closed by the same type of brackets
#   2. Opeb brackets must be closed by the correct order.

# Note: an empty string is also considered valid

# Example 1:
# Input: "()"
# Output: true

# Example 2:
# Input: "()[]{}"
# Output: true

# Example 3:
# Input: "(]"
# Output: false

# Example 4:
# Input: "{[]}"
# Output: true

# Solution 1 useing stack

class Solution1:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(0, len(s)):
            lastIndexOfStack = len(stack)-1
            if (s[i] == ')'):
                if(lastIndexOfStack >=0 and stack[lastIndexOfStack] == '('):
                    stack.pop(lastIndexOfStack)
                else:
                    stack.append(s[i])
            elif (s[i] == '}'):
                if(lastIndexOfStack >=0 and stack[lastIndexOfStack] == '{'):
                    stack.pop(lastIndexOfStack)
                else:
                    stack.append(s[i])
            elif (s[i] == ']'):
                if(lastIndexOfStack >=0 and stack[lastIndexOfStack] == '['):
                    stack.pop(lastIndexOfStack)
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])

        if (len(stack) == 0):
            return True
        else:
            return False


# Solution 2 
class Solution2:
    def isValid(self, s: str) -> bool:
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()", "").replace('{}', "").replace('[]', "")
        return s == ''

# Solution 3 using map, this one is faster
class Solution3:
    def isValid(self, s: str) -> bool:
        map = {"(": ")", "[": "]", "{": "}"}
        openSet = {"(", "[", "{"}
        stack = []

        for i in s:
            if i in openSet:
                stack.append(i)
            elif stack and i==map[stack[-1]]:
                stack.pop()
            else:
                return False
        
        return stack == []


sol = Solution3()

print("Input is '()', expected is True, mine is: ",sol.isValid("()"))
print("Input is '()[]{}', expected is True, mine is: ",sol.isValid("()[]{}"))
print("Input is '(]', expected is False, mine is: ",sol.isValid("(]"))
print("Input is '{[]}', expected is True, mine is: ",sol.isValid("{[]}"))
print("Input is '', expected is True, mine is: ",sol.isValid(""))
print("Input is '(', expected is False, mine is: ",sol.isValid("("))
print("Input is ')', expected is False, mine is: ",sol.isValid(")"))

