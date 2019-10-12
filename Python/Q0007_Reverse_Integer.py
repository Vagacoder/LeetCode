# 7. Reverse Integer
# Easy
# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:
# Input: 123
# Output: 321

# Example 2:
# Input: -123
# Output: -321

# Example 3:
# Input: 120
# Output: 21

# Note:
# Assume we are dealing with an enviroment which could only store intergers within
# the 32-bit singed integer range: [-2^31, 2^31-1]. For the purpose of this problem,
# assume that your function returns 0 when the reversed integer overflows

# Solution #1
class Solution1:
    def reverse(self, x: int) -> int:
      if (x < 0):
        isNegative:bool = True
        x = -x
      else:
        isNegative:bool = False
      
      xString: str = "" + str(x)
      resultString: str = ""

      for letter in xString:
        resultString = letter + resultString

      result: int = int(resultString)

      if (isNegative):
        result = -result

      if (result > (2**31 -1) or result < (-2**31)):
        result = 0
        
      return result


sol = Solution1()
print("Input 120, output should be 21, mine is: ", sol.reverse(120))
print("Input 123, output should be 321, mine is: ", sol.reverse(123))
print("Input -120, output should be -21, mine is: ", sol.reverse(-120))
print("Input -123, output should be -321, mine is: ", sol.reverse(-123))
