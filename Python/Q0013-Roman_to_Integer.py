# 13. Roman to Integer
# Easy

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol    Value
# I         1
# V         5
# X         10
# L         50
# C         100
# D         500
# M         1000

# For example, two is written as II in Roman numeral, just two one's added together.
# Twelve is written as, XII, which is simply X + II. The number twenty seven is written
# as XXVII, which is XX + V + II.

# Roman numeraks are usually written largest to smallest from left to right. However,
# the numeral for four is not IIII. Instead, the number four is wirtten as IV. 
# Because the one is before the five we subtract it making four. The same principle
# applies to the number nine, which is wirtten as IX, There are six instances where
# subtraction is used:
#   I can be placed before V (5) and x (10) to make 4 and 9.
#   X can be placed before L (50) and C (100) to make 40 and 90.
#   C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guranteed to be within
# the rang from 1 to 3999.

# Example 1:
# input: "III"
# output: 3

# Example 2:
# input: "IV"
# output: 4

# Example 3:
# Input: "IX"
# Output: 9

# Example 4:
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 5:
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Solution #1
class Solution1:
    def romanToInt(self, s: str) -> int:
      length = len(s)
      result = 0

      for i in range(0, length):
        if (s[i] == 'I'):
          if(i<length-1 and (s[i+1] == "V" or s[i+1] == "X")):
            result -= 1
          else:
            result += 1
        elif (s[i] == 'V'):
          result += 5
        elif (s[i] == 'X'):
          if(i<length-1 and (s[i+1] == "L" or s[i+1] == "C")):
            result -= 10
          else:
            result += 10
        elif (s[i] == 'L'):
          result += 50
        elif (s[i] == 'C'):
          if(i<length-1 and (s[i+1] == "D" or s[i+1] == "M")):
            result -= 100
          else:
            result += 100
        elif (s[i] == 'D'):
          result += 500
        elif (s[i] == 'M'):
          result += 1000

      return result

sol = Solution1()
print("Input is III, expect output is 3, mine is: ", sol.romanToInt('III'))
print("Input is IV, expect output is 4, mine is: ", sol.romanToInt('IV'))
print("Input is IX, expect output is 9, mine is: ", sol.romanToInt('IX'))
print("Input is LVIII, expect output is 58, mine is: ", sol.romanToInt('LVIII'))
print("Input is MCMXCIV, expect output is 1994, mine is: ", sol.romanToInt('MCMXCIV'))

