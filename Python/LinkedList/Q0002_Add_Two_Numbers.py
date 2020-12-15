#
# * Question 2. Add Two Numbers
# * Medium

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, 
# except the number 0 itself.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# solution 1
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode = None

    # helper function to print linked list
    def printList(self):
        print(self.val)
        if(self.next != None):
            self.next.printList()

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 != None:
            digitFromL1 = l1.val
        else:
            digitFromL1 = 0
        if l2 != None:
            digitFromL2 = l2.val
        else:
            digitFromL2 = 0

        sumOfdigits = digitFromL1 + digitFromL2
        digitOfResult = sumOfdigits % 10
        carrier = sumOfdigits // 10
        result = ListNode(digitOfResult)
        cursor = result
        l1 = l1.next
        l2 = l2.next

        while (l1 != None or l2 != None):
            if l1 != None:
                digitFromL1 = l1.val
                l1 = l1.next
            else:
                digitFromL1 = 0
            if l2 != None:
                digitFromL2 = l2.val
                l2 = l2.next
            else:
                digitFromL2 = 0
            sumOfdigits = digitFromL1 + digitFromL2 + carrier
            digitOfResult = sumOfdigits % 10
            carrier = sumOfdigits // 10
            cursor.next = ListNode(digitOfResult)
            cursor = cursor.next

        if carrier > 0:
            cursor.next = ListNode(carrier)
        return result

# list1 = [2, 4, 3]
list1 = [2,4,3]
l1 = ListNode(list1[0])
cursor = l1
for i in range(1, len(list1)):
    cursor.next = ListNode(list1[i])
    cursor = cursor.next

# list2 = [5, 6, 4]
list2 = [5,6,4]
l2 = ListNode(list2[0])
cursor = l2
for i in range(1, len(list2)):
    cursor.next = ListNode(list2[i])
    cursor = cursor.next


sol = Solution()
print(sol.addTwoNumbers(l1, l2).printList())