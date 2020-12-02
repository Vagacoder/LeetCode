# Question 1. Two Sum
# Easy
# Given an array of integers, return indices of the two numbers such that
# they add up to a specific target. You may assume that each input would
# have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

#%%
from typing import List

class Solution:
    # * Solution 1,  Brutal Force ( O(n^2) )
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        numsLen = len(nums)
        for i in range(numsLen):
            for j in range(i+1, numsLen):
                if ((nums[i] + nums[j]) == target):
                    return [i, j]
        return[-1, -1]


    # * Solution 2, Hash ( O(n) )
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        numsLen = len(nums)
        # temporay dic to store key-value pair:
        # key is difference betweem target and nums[index];
        # value is index of element in nums
        indexList = {}
        for i in range(numsLen):
            difference = target - nums[i]
            if nums[i] in indexList:
                return [indexList[nums[i]], i]
            else:
                indexList[difference] = i
        return [-1, -1]


    # * Solution 3, using array, it may out of bound.
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        numsLen = len(nums)
        checkList = [-1] * (1000)
        for i in range(numsLen):
            if checkList[target - nums[i]] != -1:
                return [i, checkList[target - nums[i]]]
            else:
                checkList[nums[i]] = i

        return [-1, -1]


    # * Solution 4, Sorting first, then using two pointers ( O(n) )
    def twoSum4(self, nums: List[int], target: int) -> List[int]:
        numsLen: int = len(nums)
        # ! Sort
        nums.sort()
        # ! Two pointers
        low: int = 0
        high: int = numsLen - 1

        while high > low:
            currentSum: int = nums[low] + nums[high]
            if currentSum == target:
                return [low, high]
            elif currentSum < target:
                low += 1
            else:
                high -= 1

        return [-1, -1]


sol = Solution()

nums1 = [1, 2, 3, 7, 11, 15]
nums2 = [2, 11, 7, 15]
nums3 = [1, 2, 7]
nums4 = [-3, 4, 3, 90]
target1 = 9

print(sol.twoSum4(nums1, target1))
print(sol.twoSum4(nums2, target1))
print(sol.twoSum4(nums3, target1))
print(sol.twoSum4(nums4, target1))

# %%
