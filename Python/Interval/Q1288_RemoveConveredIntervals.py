#
# * 1288. Remove Covered Intervals
# * Medium

# * Given a list of intervals, remove all intervals that are covered by another 
# * interval in the list.

# * Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

# * After doing so, return the number of remaining intervals.

 

# * Example 1:

# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

# * Example 2:

# Input: intervals = [[1,4],[2,3]]
# Output: 1

# * Example 3:

# Input: intervals = [[0,10],[5,12]]
# Output: 2

# * Example 4:

# Input: intervals = [[3,10],[4,10],[5,11]]
# Output: 2

# * Example 5:

# Input: intervals = [[1,2],[1,4],[3,4]]
# Output: 1

# * Constraints:

#     1 <= intervals.length <= 1000
#     intervals[i].length == 2
#     0 <= intervals[i][0] < intervals[i][1] <= 10^5
#     All the intervals are unique.

#%%

class Solution:

    # * Solution 1
    def removeCoveredIntervals1(self, intervals: list) -> int:
        import functools

        n = len(intervals)

        def sortIntervals(i1, i2):
            if i1[0] == i2[0]:
                return i2[1] - i1[1]
            else:
                return i1[0] - i2[0]
        
        # print(intervals)

        # ! functools.cmp_to_key()
        intervals = sorted(intervals, key=functools.cmp_to_key(sortIntervals))

        # print(intervals)

        # newintv = intervals.sort(key= functools.cmp_to_key(sortIntervals))
        # print(newintv)

        left = intervals[0][0]
        right = intervals[0][1]

        count = 0

        for i in range(1, n):
            intv = intervals[i]
            # * find covered
            if left <= intv[0] and intv[1] <= right:
                count += 1
            # * find crossed 
            elif intv[0] <= right and right <= intv[1]:
                right = intv[1]
            # * find no cross, no covered
            elif right < intv[0]:
                left = intv[0]
                right = intv[1]

        return n - count


    # * Solution 2
    def removeCoveredIntervals2(self, intervals: list) -> int:

        left = -1
        right = -1
        result = 0

        # * sort by interval start
        intervals.sort(key=lambda x: x[0])

        print(intervals)

        for intv in intervals:
            if left < intv[0] and right < intv[1]:
                left = intv[0]
                result +=1
            
            right = max(right, intv[1])
        
        return result


    # * Solution 3
    # ! simple 
    def removeCoveredIntervals3(self, intervals: list) -> int:
        left = -1
        right = -1
        result = 0

        # ! simple implementation
        intervals.sort(key=lambda x: x[0])

        for intv in intervals:
            if left < intv[0] and right < intv[1]:
                left = intv[0]
                result +=1
            
            right = max(right, intv[1])
        
        return result


sol = Solution()
intv1 = [[1,4],[3,6],[2,8]]
r1 = sol.removeCoveredIntervals3(intv1)
print('ex: {}, re: {}'.format(2, r1))

intv1 = [[1,4],[2,3]]
r1 = sol.removeCoveredIntervals3(intv1)
print('ex: {}, re: {}'.format(1, r1))

intv1 = [[0,10],[5,12]]
r1 = sol.removeCoveredIntervals3(intv1)
print('ex: {}, re: {}'.format(2, r1))

intv1 = [[3,10],[4,10],[5,11]]
r1 = sol.removeCoveredIntervals3(intv1)
print('ex: {}, re: {}'.format(2, r1))

intv1 = [[1,2],[1,4],[3,4]]
r1 = sol.removeCoveredIntervals3(intv1)
print('ex: {}, re: {}'.format(1, r1))
