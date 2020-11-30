#
# * 56. Merge Intervals
# * Medium

# * Given an array of intervals where intervals[i] = [starti, endi], merge all 
# * overlapping intervals, and return an array of the non-overlapping intervals 
# * that cover all the intervals in the input.

# * Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# * Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

 

# * Constraints:

#     1 <= intervals.length <= 104
#     intervals[i].length == 2
#     0 <= starti <= endi <= 104

#%%
class Solution:

    # * Solution 1
    def merge1(self, intervals: list) -> list:
        intervals.sort(key=lambda x: x[0])
        print(intervals)

        left = intervals[0][0]
        right = intervals[0][1]

        n = len(intervals)
        result = []
        for i in range(1, n):
            # print('left:', left)
            # print('right:', right)

            intv = intervals[i]

            # print('intv:', intv)

            if intv[0] <= right:
                # print('merge')
                right = max(right, intv[1])
            elif right < intv[0]:
                # print('new ')
                result.append([left, right])
                left = intv[0]
                right = intv[1]

        result.append([left, right])
        return result

sol = Solution()
i1 = [[1,3],[2,6],[8,10],[15,18]]
r1 = sol.merge1(i1)
print(r1)

i1 = [[1,4],[4,5]]
r1 = sol.merge1(i1)
print(r1)