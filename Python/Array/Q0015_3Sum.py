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

#%%
from typing import List

class Solution:
    # * Solution 1 brutal force O(N^3) exceed time limit
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
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

    # * Solution 2 faster but still exceed time limit
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
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
                    # temp.sort()
                    if not temp in result:
                        result.append(temp)
                    high -= 1
                    low += 1

        return result

    # * Solution 3 still exceed time limit
    def threeSum3(self, nums: List[int]) -> List[List[int]]:
        numPool = {}
        if len(nums) > 0:
            numPool[nums[0]] = 0
        N: int = len(nums)
        result = []
        for i in range(N):
            for j in range(i+1, N):
                sumOfIandJ = nums[i] + nums[j]
                if (-sumOfIandJ in numPool) and (numPool)[-sumOfIandJ] != i and (numPool)[-sumOfIandJ] != j:
                    temp = [nums[i], nums[j], -(nums[i] + nums[j])]
                    temp.sort()
                    if not temp in result:
                        result.append(temp)
                else:
                    numPool[nums[j]] = j

        return result


    # * Solution 4, Sorting + 2 Pointers
    def threeSum4(self, nums: list, target: int)-> list:
        nums.sort()

        # print(nums)

        n = len(nums)
        result =[]

        # ! i for 1st number, low (left) for 2nd number,  high (right) for 3rd number
        for i in range(n):
            
            # * skip repeated 1st number
            if i > 0 and nums[i] == nums[i-1]:
                continue

            currentI = nums[i]
            low = i+1
            high = n-1

            while high > low:
                left = nums[low]
                right = nums[high]
                
                # print(i, low, high, currentSum)

                if currentI + left + right == target:
                    result.append([nums[i], nums[low], nums[high]])
                    
                    # * skip repeated 2nd and 3rd numbers
                    while nums[low] == left and low < high:
                        low += 1

                    while nums[high] == right and low < high:
                        high -= 1

                elif currentI + left + right > target:
                    
                    # * skip repeated 3rd number
                    while low < high and nums[high] == right:
                        high -= 1
                else:
                    # * skip repeated 2nd number
                    while low < high and nums[low] == left :
                        low += 1

        return result


    # * Solution 5, Hash
    def threeSum5(self, nums: list, target: int)-> list:
        n = len(nums)
        value2IndexDict = {}

        for index in range(n):
            value = nums[index]
            value2IndexDict[value] = index

        result = set()
        for i in range(n):
            for j in range(i+1, n):
                diff = target - nums[i] - nums[j]
                if (diff in value2IndexDict) and i != value2IndexDict[diff] and j != value2IndexDict[diff]:
                    temp = sorted([nums[i], nums[j], diff])
                    result.add(tuple(temp))
        
        return [list(x) for x in result]


sol = Solution()
a = [-1, 0, 1, 2, -1, -4]
b = []
c = [0]
d = [1]
e = [0,0,0,0]
print(sol.threeSum5(a, 0))
print(sol.threeSum5(b, 0))
print(sol.threeSum5(c, 0))
print(sol.threeSum5(d, 0))
print(sol.threeSum5(e, 0))

# %%
