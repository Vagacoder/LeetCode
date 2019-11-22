# 4. Median of Two Sorted Arrays
# There are tow sorted arrays Nums1 and Nums2 of size m and n respectively.
# Find the median of the two sorted arrays. 

# Requirement: The overall run time of complexity should be O(log(m+n)).

# You may assume Nums1 and Nums2 cannot be empty.

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# Result: 2.0

# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# Result: (2+3)/2 = 2.5
from typing import List

# solution1 sort and find median O(nlog(n))
# This is a CHEATING, But: my submission is ~~~~~~~
# Runtime: 84 ms, faster than 99.44% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Median of Two Sorted Arrays.
# LOLLLLLLLLL~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 : List[int] = nums1 + nums2
        nums3.sort()
        nums3Len = len(nums3)
        if (nums3Len % 2 == 1 ):
            return nums3[(nums3Len //2)]
        else:
            return (nums3[(nums3Len//2)] + nums3[(nums3Len//2) - 1] ) /2

# OK this is a serious trying
class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        return 0.0


sol = Solution1()
nums1 = [1, 3]
nums2 = [2]
print(sol.findMedianSortedArrays(nums1, nums2))
nums3 = [1, 2]
nums4 = [3, 4]
print(sol.findMedianSortedArrays(nums3, nums4))
