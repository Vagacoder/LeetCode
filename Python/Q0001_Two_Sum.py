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

# solution 1 brutal force ( O(n^2) )
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsLen = len(nums)
        for i in range(numsLen):
            for j in range(i+1, numsLen):
                if ((nums[i] + nums[j]) == target):
                    return [i,j]
        return[-1, -1]


# solution 2 ( O(n) )
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsLen = len(nums)
        # temporay dic to store key-value pair: 
        # key is difference betweem target and nums[index];
        # value is index of element in nums
        indexList = {}
        for i in range(numsLen):
            difference = target - nums[i]
            if nums[i] in indexList :
                return [indexList[nums[i]], i]
            else :
                indexList[difference] = i
        return [-1, -1]

# solution 3 using array, it may out of bound.
class Solution2:
    def twoSum(self, nums: List[int], targe: int) -> List[int]:
        numsLen = len(nums)
        checkList = [-1]* (1000)
        for i in range(numsLen):
            if checkList[targe - nums[i]] != -1:
                return [i, checkList[targe - nums[i]]]
            else:
                checkList[nums[i]] = i
        
        return [-1, -1]


sol = Solution2()

nums1 = [1, 2, 3, 7, 11, 15]
nums2 =[2, 7 , 11, 15]
nums3 = [1, 2, 7]
nums4 = [-3, 4, 3, 90] 
target1 = 9

print(sol.twoSum(nums1, target1))
print(sol.twoSum(nums2, target1))
print(sol.twoSum(nums3, target1))
print(sol.twoSum(nums4, target1))
