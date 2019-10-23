# 21. Merge Two Sorted Lists
# Easy

# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the
# first two lists

# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution 1
class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # check special cases
        if (l1 == None and l2 == None):
            return None

        if (l1 == None and l2 != None):
                return l2
        
        if (l2 == None and l1 != None):
                return l1
        
        # normal case
        cur1 = l1
        cur2 = l2

        # determine root
        if(cur1.val> cur2.val):
            root = ListNode(cur2.val)
            cur = root
            cur2 = cur2.next
        else :
            root = ListNode(cur1.val)
            cur = root
            cur1 = cur1.next

        # extending list
        while (cur1 != None or cur2 != None):
            if (cur1 == None):
                cur.next = ListNode(cur2.val)
                cur = cur.next
                cur2 = cur2.next
                continue
            if (cur2 == None):
                cur.next = ListNode(cur1.val)
                cur = cur.next
                cur1 = cur1.next
                continue
            if(cur1.val > cur2.val):
                cur.next = ListNode(cur2.val)
                cur = cur.next
                cur2 = cur2.next
            else:
                cur.next = ListNode(cur1.val)
                cur = cur.next
                cur1 = cur1.next

        return root

# Solution 2, recursove way, super awesome
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # check special cases
        if (l1 == None):
                return l2
        if (l2 == None):
                return l1
        
        # normal case
        cur1 = l1
        cur2 = l2

        # determine root
        if(cur1.val> cur2.val):
            root = cur2
            cur2.next = self.mergeTwoLists(cur1, cur2.next)
        else :
            root = cur1
            cur1.next =self.mergeTwoLists(cur1.next, cur2)
        
        return root

 


sol = Solution2()

l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_3 = ListNode(4)
l1_1.next = l1_2
l1_2.next = l1_3


l2_1 = ListNode(1)
l2_2 = ListNode(3)
l2_3 = ListNode(4)
l2_1.next = l2_2
l2_2.next = l2_3

# l1_1 = None
# l2_1 = None

print("test1, expect 1, 1, 2 ,3, 4, 4, mine is: ")
lresult = sol.mergeTwoLists(l1_1, l2_1)
cur = lresult
while (cur != None):
    print(cur.val)
    cur = cur.next

