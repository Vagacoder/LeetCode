#
# * 986. Interval List Intersections
# * Medium

# * Given two lists of closed intervals, each list of intervals is pairwise disjoint 
# * and in sorted order.

# * Return the intersection of these two interval lists.

# * (Formally, a closed interval [a, b] (with a <= b) denotes the set of real 
# * numbers x with a <= x <= b.  The intersection of two closed intervals is a 
# * set of real numbers that is either empty, or can be represented as a closed 
# * interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

# * Example 1:

# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

# *Note:

#     0 <= A.length < 1000
#     0 <= B.length < 1000
#     0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

#%%

class Solution:
    
    # * Solution 1
    def intervalIntersection(self, A: list, B: list) -> list:
        i = 0
        j = 0
        n = len(A)
        m = len(B)
        result = []
        while i < n and j < m:
            a1, a2 = A[i][0], A[i][1]
            b1, b2 = B[j][0], B[j][1]
            if b2 >= a1 and a2 >= b1:
                result.append([max(a1,b1),min(a2, b2)])
            if b2 > a2:
                i+=1
            else:
                j+=1

        return result

    
sol = Solution()
a1 = [[0,2],[5,10],[13,23],[24,25]]
b1 = [[1,5],[8,12],[15,24],[25,26]]
r1 = sol.intervalIntersection(a1, b1)
print(r1)

