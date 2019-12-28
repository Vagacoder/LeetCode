# Question 15. 3Sum
# Medium
# Given an array nums of n integers, are there elements a, b, c in nums such that
# a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note: The solution set must not contain duplicate triplets.

# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#  [-1, 0, 1],
#  [-1, -1, 2]
# ]

from typing import List

# Solution 1 brutal force O(N^3)


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N: int = len(nums)
        result = []
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    if (nums[i] + nums[j] + nums[k] == 0):
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        if not temp in result:
                            result.append(temp)

        return result

# Solution 2 faster


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N: int = len(nums)
        result = []
        for i in range(N):
            low = i + 1
            high = N - 1

            while high > low:
                if nums[low] + nums[high] > -nums[i]:
                    high -= 1
                elif nums[low] + nums[high] < -nums[i]:
                    low += 1
                else:
                    temp = [nums[i], nums[low], nums[high]]
                    temp.sort()
                    if not temp in result:
                        result.append(temp)

        return result


sol = Solution2()
a = [-1, 0, 1, 2, -1, -4]
# b = []
# c = [0]
# d = [1]
print(sol.threeSum(a))
# print(sol.threeSum(b))
# print(sol.threeSum(c))
# print(sol.threeSum(d))
