#
# * 18. 4Sum
# * Medium

# * Given an array nums of n integers and an integer target, are there elements 
# * a, b, c, and d in nums such that a + b + c + d = target? Find all unique 
# * quadruplets in the array which gives the sum of target.

# * Notice that the solution set must not contain duplicate quadruplets.

# * Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# * Example 2:

# Input: nums = [], target = 0
# Output: []

# * Constraints:

#     0 <= nums.length <= 200
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109

#%%
class Solution:

    # * Solution 1, All based on Q15, 3Sum
    def fourSum1(self, nums: list, target: int) -> list:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            currentI = nums[i]

            for j in range(i+1, n):
                if j > i+1 and nums[j] ==nums[j-1]:
                    continue

                currentJ = nums[j]
                low = j+1
                high = n-1

                while high > low:
                    left = nums[low]
                    right = nums[high]

                    if currentI + currentJ + left + right == target:
                        result.append([nums[i], nums[j], nums[low], nums[high]])

                        while nums[low] == left and low < high:
                            low += 1
                        while nums[high] == right and low < high:
                            high -= 1
                    elif currentI + currentJ + left + right > target:
                        while low < high and nums[high] == right:
                            high -= 1
                    else:
                        while low < high and nums[low] == left:
                            low +=1

        return result 
                    


sol = Solution()
n1 = [1,0,-1,0,-2,2]
t1 = 0
r1 = sol.fourSum1(n1, t1)
print(r1)

n1 = []
t1 = 0
r1 = sol.fourSum1(n1, t1)
print(r1)

# %%
