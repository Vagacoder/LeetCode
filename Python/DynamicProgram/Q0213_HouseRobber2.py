#
# * 213. House Robber II
# * Medium

# * You are a professional robber planning to rob houses along a street. Each house 
# * has a certain amount of money stashed. All houses at this place are arranged 
# * in a circle. That means the first house is the neighbor of the last one. 
# * Meanwhile, adjacent houses have a security system connected, and it will 
# * automatically contact the police if two adjacent houses were broken into on 
# * the same night.

# Given a list of non-negative integers nums representing the amount of money of 
# each house, return the maximum amount of money you can rob tonight without 
# alerting the police.


# * Example 1:

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

# * Example 2:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# * Example 3:

# Input: nums = [0]
# Output: 0


# * Constraints:

#     1 <= nums.length <= 100
#     0 <= nums[i] <= 1000

#%%

class Solution:

    # * Solution 1
    def rob1(self, nums: list) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])


        def robRange(start:int, end:int)->int:
            dp = [0] * n
            dp[start] = nums[start]
            dp[start+1] = max(nums[start], nums[start+1])
            for i in range(start+2,end+1):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])

            return dp[end]


        return max(robRange(0, n-2), robRange(1, n-1))



sol = Solution()
nums = [2,3,2]
r1 = sol.rob1(nums)
print(r1)


# %%
