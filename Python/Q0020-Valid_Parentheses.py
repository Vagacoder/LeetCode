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

# Solution 1
class Solution1:
    def isValid(self, s: str) -> bool:
        
        return True


sol = Solution1()
print(sol.isValid("()"))
