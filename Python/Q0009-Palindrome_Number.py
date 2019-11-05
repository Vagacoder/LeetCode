# 9. Palindrome Number
# Easy

# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.

# Example 1:
# Input: 121
# Output: true

# Example 2:
# Input: -121
# Output: false
# Explaination: From left to right, it reads -121; From right to left, it reads
# 121-, not same

# Example 3:
# Input: 10
# Output: false

# Follow up:
# Coud you solve it without converting the integer to a string?

# Solution 1 (to string)


class Solution1:
    def isPalindrome(self, x: int) -> bool:
        xString: str = str(x)
        return self.isPalindromeString(xString)

    def isPalindromeString(self, xString: str) -> bool:
        if (len(xString) == 1):
            return True
        elif (len(xString) == 2):
            return (xString[0] == xString[1])
        else:
            return ((xString[0] == xString[-1]) and self.isPalindromeString((xString[1: -1])))

# Solution 2 (reverse half of the number)


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0 or (x % 10 == 0 and x != 0)):
            return False

        revertedNum = 0
        while (x > revertedNum):
            revertedNum = revertedNum * 10 + x % 10
            x = x//10

        return x == revertedNum or x == revertedNum//10


sol = Solution2()
print("Input is 121, output should be True, mine is: ", sol.isPalindrome(121))
print("Input is 1121, output should be False, mine is: ", sol.isPalindrome(-121))
print("Input is 10, output should be False, mine is: ", sol.isPalindrome(10))
print("Input is 1, output should be True, mine is: ", sol.isPalindrome(1))
print("Input is 11, output should be True, mine is: ", sol.isPalindrome(11))
print("Input is 1021, output should be False, mine is: ", sol.isPalindrome(1021))
print("Input is 1000021, output should be False, mine is: ",
      sol.isPalindrome(1000021))
