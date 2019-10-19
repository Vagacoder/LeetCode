# Q 12. Integer to Roman
# Medium

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, two is written as II in Roman numeral, just two one's added together.
# Tweleve is written as XII, which is simply X + II. The number twenty seven is 
# written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right.
# However, numeral for four is not IIIIm. Instead, the numbers four is wirtten as
# IV, because the one is before the five we subtract it making four. The same
# principle applies to the number nine, which is written as IX. There are six
# instance where substraction is used:


#   I can be placed before V (5) and X (10) to make 4 and 9. 
#   X can be placed before L (50) and C (100) to make 40 and 90. 
#   C can be placed before D (500) and M (1000) to make 400 and 900.

# Given an integer, convert it to a roman numeral. Input is guaranteed to be
# within the range from 1 to 3999.

# Example 1:
# Input: 3
# Output: III

# Example 2:
# Input: 4
# Output: IV

# Example 3:
# Input: 9
# Output: IX

# Example 4:
# Input: 58
# Output: LVIII

# Example 5:
# Input: 1994
# Output: MCMXCIV

# Soultion 1, turn to string
class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""

        inputStr = str(num)
        length = len(inputStr)
        for i in range(length-1, -1, -1):
            if(inputStr[i] == '0'):
                continue
            digit = length-1-i
            # check ones
            if(digit == 0):
                if (inputStr[i] == '1'):
                    result += "I"
                elif (inputStr[i] == '2'):
                    result += "II"
                elif (inputStr[i] == '3'):
                    result += "III"
                elif (inputStr[i] == '4'):
                    result += "IV"
                elif (inputStr[i] == '5'):
                    result += "V"
                elif (inputStr[i] == '6'):
                    result += "VI"
                elif (inputStr[i] == '7'):
                    result += "VII"
                elif (inputStr[i] == '8'):
                    result += "VIII"
                elif (inputStr[i] == '9'):
                    result += "IX"
            # check tens
            elif(digit == 1):
                if (inputStr[i] == '1'):
                    result = "X" + result
                elif (inputStr[i] == '2'):
                    result = "XX" + result
                elif (inputStr[i] == '3'):
                    result = "XXX" + result
                elif (inputStr[i] == '4'):
                    result = "XL" + result
                elif (inputStr[i] == '5'):
                    result = "L" + result
                elif (inputStr[i] == '6'):
                    result = "LX" + result
                elif (inputStr[i] == '7'):
                    result = "LXX" + result
                elif (inputStr[i] == '8'):
                    result = "LXXX" + result
                elif (inputStr[i] == '9'):
                    result = "XC" + result
            # check hundreds
            elif(digit == 2):
                if (inputStr[i] == '1'):
                    result = "C" + result
                elif (inputStr[i] == '2'):
                    result = "CC" + result
                elif (inputStr[i] == '3'):
                    result = "CCC" + result
                elif (inputStr[i] == '4'):
                    result = "CD" + result
                elif (inputStr[i] == '5'):
                    result = "D" + result
                elif (inputStr[i] == '6'):
                    result = "DC" + result
                elif (inputStr[i] == '7'):
                    result = "DCC" + result
                elif (inputStr[i] == '8'):
                    result = "DCCC" + result
                elif (inputStr[i] == '9'):
                    result = "CM" + result
            # check thousands
            elif(digit == 3):
                if (inputStr[i] == '1'):
                    result = "M" + result
                elif (inputStr[i] == '2'):
                    result = "MM" + result
                elif (inputStr[i] == '3'):
                    result = "MMM" + result
                else:
                    continue
            else:
                continue
        return result

sol = Solution()
print("Input is 3, expected III, mine is: ", sol.intToRoman(3))
print("Input is 30, expected III, mine is: ", sol.intToRoman(30))
print("Input is 4, expected IV, mine is: ", sol.intToRoman(4))
print("Input is 9, expected IX, mine is: ", sol.intToRoman(9))
print("Input is 58, expected LVIII, mine is: ", sol.intToRoman(58))
print("Input is 1994, expected MCMXCIV, mine is: ", sol.intToRoman(1994))


