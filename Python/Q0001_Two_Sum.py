# Question 1. Two Sum
# Easy
# Given an array of integers, return indices of the two numbers such that 
# they add up to a specific target. You may assume that each input would 
# have exactly one solution, and you may not use the same element twice.

#Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
from typing import List

nums = [1, 2, 3, 7, 11, 15]
target = 9

# solution 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsLen = len(nums)
        for i in range(numsLen):
            for j in range(i+1, numsLen):
                if ((nums[i] + nums[j]) == target):
                    return [i,j]
        return[-1, -1]



sol = Solution()
print(sol.twoSum(nums, target))