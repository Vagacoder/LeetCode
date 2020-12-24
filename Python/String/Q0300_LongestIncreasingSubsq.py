#
# * 300. Longest Increasing Subsequence
# * Medium

# * Given an integer array nums, return the length of the longest strictly increasing 
# * subsequence.

# * A subsequence is a sequence that can be derived from an array by deleting some 
# * or no elements without changing the order of the remaining elements. For example, 
# * [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

# * Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# * Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4

# * Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

# * Constraints:

#     1 <= nums.length <= 2500
#     -104 <= nums[i] <= 104

 

# Follow up:

#     Could you come up with the O(n2) solution?
#     Could you improve it to O(n log(n)) time complexity?

#%%

class Solution:
    # * Solution 1
    # ! Dynamic Programming
    def lengthOfLIS(self, nums: list) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                dp[i] = max(dp[i], dp[j]+1)

        return max(dp)


    # * Solution 2
    # ! Patience Sorting + Binary Search !
    def lengthOfLIS2(self, nums:list)-> int:
        pass


    # * Solution 3
    # ! Recursive
    def lengthOfLIS3(self, nums:list)-> int:
        def lisHelper(nums:list, preVal: int, cur: int):
            # * Base case
            if cur == len(nums):
                return 0

            includeThis = 0
            if nums[cur] > preVal:
                includeThis = 1 + lisHelper(nums, nums[cur], cur+1)
            
            notIncludeThis = lisHelper(nums, preVal, cur+1)

            return max(includeThis, notIncludeThis)

        return lisHelper(nums, min(nums)-1, 0)




sol = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
r1 = sol.lengthOfLIS3(nums)
print(r1)

nums = [0,1, 0, 3, 2, 3]
r1 = sol.lengthOfLIS3(nums)
print(r1)


nums = [7,7,7,7,7,7,7,7]
r1 = sol.lengthOfLIS3(nums)
print(r1)
        