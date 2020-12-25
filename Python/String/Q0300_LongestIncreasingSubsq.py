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
    # !!! Patience Sorting + Binary Search !!!
    # TODO
    def lengthOfLIS2(self, nums:list)-> int:

        # # * Helper of binary search in list
        # def binarySearch(vals:list, start:int, end: int, val:int)->int:
        #     if start > end:
        #         return end;

        #     middle = (start + end)//2

        #     if vals[middle] == val:
        #         return middle
        #     elif vals[middle] > val:
        #         return binarySearch(vals, start, middle-1, val)
        #     elif vals[middle] < val:
        #         return binarySearch(vals, middle+1, end, val)


        dp = [-1] * len(nums)
        piles = 0

        for num in nums:
            left = 0
            right = piles
            while left != right:
                middle = (left + right) // 2
                if dp[middle] < num:
                    left = middle + 1
                else:
                    right = middle
            
            dp[left] = num
            piles = max(left+1, piles)

        return piles


    # * Solution 3
    # ! Recursive, Actually is same as Solution 1, 
    # ! TLE
    def lengthOfLIS3(self, nums:list)-> int:

        # * Recursive helper
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


    # * Solution 4
    # ! Recursive with memo, improved from Solution 3.
    # ! Still TLE
    def lengthOfLIS4(self, nums:list)-> int:
        
        memo = [[-1]*len(nums) for _ in range(len(nums)+1) ]
        # print(memo)

        # * Recursive helper
        def lisHelper(nums:list, preIndex:int, cur:int):
            # * Base case 
            if cur == len(nums):
                return 0;
            
            if memo[preIndex+1][cur] >= 0:
                return memo[preIndex+1][cur]
            
            includeThis = 0
            if preIndex < 0 or nums[cur] > nums[preIndex]:
                includeThis  = 1 + lisHelper(nums, cur, cur+1)
            
            notIncludeThis = lisHelper(nums, preIndex, cur+1)
            memo[preIndex+1][cur] = max(includeThis, notIncludeThis)
            return memo[preIndex+1][cur]

        return lisHelper(nums, -1, 0)



sol = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
r1 = sol.lengthOfLIS2(nums)
print(r1)

nums = [0,1, 0, 3, 2, 3]
r1 = sol.lengthOfLIS2(nums)
print(r1)


nums = [7,7,7,7,7,7,7,7]
r1 = sol.lengthOfLIS2(nums)
print(r1)

# # * Helper of binary search in list
# # TODO
# def binarySearch(vals:list, start:int, end: int, val:int)->int:
#     if start > end:
#         return end;

#     middle = (start + end)//2

#     if vals[middle] == val:
#         return middle
#     elif vals[middle] > val:
#         return binarySearch(vals, start, middle-1, val)
#     elif vals[middle] < val:
#         return binarySearch(vals, middle+1, end, val)

# n1 = [10, 11, 12, 13, 14]
# print(binarySearch(n1, 0, 3, 10))
# print(binarySearch(n1, 0, 3, 11))
# print(binarySearch(n1, 0, 3, 13))
# print(binarySearch(n1, 0, 3, 14))
# print(binarySearch(n1, 1, 3, 10))
# print(binarySearch(n1, 1, 3, 9))
# print(binarySearch(n1, 1, 3, 14))

# n2 = [21, 22, 24, 25, 26]
# print(binarySearch(n1, 0, 3, 23))


        