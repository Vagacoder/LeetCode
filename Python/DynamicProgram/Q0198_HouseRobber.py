#
# * 198. House Robber
# * Easy

# * You are a professional robber planning to rob houses along a street. Each 
# * house has a certain amount of money stashed, the only constraint stopping you 
# * from robbing each of them is that adjacent houses have security system connected 
# * and it will automatically contact the police if two adjacent houses were broken 
# * into on the same night.

# Given a list of non-negative integers representing the amount of money of each 
# house, determine the maximum amount of money you can rob tonight without alerting 
# the police.

 

# * Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.

# * Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.

 
# * Constraints:

#     0 <= nums.length <= 100
#     0 <= nums[i] <= 400

#%%

class Solution:

    # * Solution 1, Dynamic, from top to bottom
    def rob1(self, nums: list) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[n-1]


    # * Solution 1.1, Dynamic, from top to bottpm, Optimized
    def rob1e(self, nums: list) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp0 = nums[0]
        dp1 = max(nums[0], nums[1])
        dp2 = max(dp0, dp1) 
        # * or dp2 = dp1

        for i in range(2, n):
            dp2 = max(dp1, dp0 + nums[i])
            dp0 = dp1
            dp1 = dp2
        
        return dp2


    # * Solution 2, Recursive, from top to bottom
    # ! Too slow, TLE
    def rob2(self, nums: list) -> int:

        def dp(nums, index):
            # * Base case:
            if index >= len(nums):
                return 0

            # * Recursive calls
            result = max(dp(nums, index+1), (nums[index]+dp(nums, index+2)))
            return result
    
        return dp(nums, 0)



    # * Solution 3, Recursive, from top to bottom with MEMO
    # * From solution 2
    def rob3(self, nums: list) -> int:
        # * initialize memo
        memo = [-1] * len(nums)
        
        def dp(nums, index):
            # * Base case:
            if index >= len(nums):
                return 0

            # * check memo
            if memo[index] != -1:
                return memo[index]

            # * Recursive calls
            result = max(dp(nums, index+1), (nums[index]+dp(nums, index+2)))

            # * add result to memo
            memo[index] = result
            
            return result

        return dp(nums, 0)


    # * Solution 4, Dynamic, from bottom to top
    def rob4(self, nums: list) -> int:
        n = len(nums)

        # * initial dp, we need check dp[i+2], so length of dp is n+2
        dp = [0] * (n+2)

        # * rob from last house to first house
        for i in range(n-1, -1, -1):
            dp[i] = max(dp[i+1], nums[i] + dp[i+2])

        # * max profit at first house
        return dp[0]


    # * Solution 5, Dynamic, from bottom to top, with optimization
    def rob5(self, nums: list) -> int:
        n = len(nums)

        # * record dp[i+1], dp[i+2]
        dpi1 = 0
        dpi2 = 0

        # * record dp[i]
        dpi = 0
        for i in range(n-1, -1, -1):
            dpi = max(dpi1, nums[i] + dpi2)
            dpi2 = dpi1
            dpi1 = dpi

        return dpi



sol = Solution()

nums = [1,2,3,1]
r1 = sol.rob5(nums)
print(r1)

nums = [2,7,9,3,1]
r1 = sol.rob5(nums)
print(r1)
# %%
