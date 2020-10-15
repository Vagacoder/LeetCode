# 26. Remove Duplicates from Sorted Array
# Easy

# Given a sorted array nums, remove the duplicates in-place such that each element
# appears only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the
# input array in-place with O(1) extra memory.

# Example 1:
# given nums = [1, 1, 2],
# your function should return length = 2, since array will be [1, 2]

# Example 2:
# given number = [0,0,1,1,1,2,2,3,3,4],
# your function should return length = 5, with the array of [0, 1, 2, 3, 4]

# Clarification:
# Confused why the returned value is an integer but your answer is an array?
# Note that he input array is passed in by reference
from typing import List

# Solution1, using 2 pointers, and treat list as array which cannot change size.
class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums) == 0 or len(nums) == 1):
            return len(nums)
        
        backCurIndex = 0
        frontCurIndex = 1
        lastNumber = nums[backCurIndex] 
        moveStep = 0
        while (frontCurIndex < len(nums)):
            if (nums[frontCurIndex] == lastNumber):
                frontCurIndex+=1
                moveStep+=1
            else:
                nums[frontCurIndex - moveStep] = nums[frontCurIndex]
                frontCurIndex+=1
                backCurIndex+=1
                lastNumber = nums[backCurIndex] 

        return backCurIndex+1

sol=Solution1()
print("input [], expected 0, mine is: ", sol.removeDuplicates([]))
print("input [1], expected 1, mine is: ", sol.removeDuplicates([1]))
print("input [1,1], expected , mine is: ", sol.removeDuplicates([1,1]))
print("input [1,1,1], expected 1, mine is: ", sol.removeDuplicates([1,1,1]))
print("input [1,1,2], expected 2, mine is: ", sol.removeDuplicates([1,1,2]))
print("input [1,1,2], expected 2, mine is: ", sol.removeDuplicates([1,2,2,2,2,2]))
print("input [0,0,1,1,1,2,2,3,3,4], expected 5, mine is: ", sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

