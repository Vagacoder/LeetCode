#
# * 141. Linked List Cycle
# * Easy

# * Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be 
# reached again by continuously following the next pointer. Internally, pos is 
# used to denote the index of the node that tail's next pointer is connected to. 
# * Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# * Example 1:

# * 3 -> 2 -> 0 -> 4
# *      |         |
# *      ----------

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to 
# the 1st node (0-indexed).

# * Example 2:

# * 1 -> 2
# * |    |
# * -----

# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# * Constraints:

#     The number of the nodes in the list is in the range [0, 104].
#     -105 <= Node.val <= 105
#     pos is -1 or a valid index in the linked-list.

# ? Follow up: Can you solve it using O(1) (i.e. constant) memory?


#%%

# * Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # * Solution 1
    # * Space O(n)
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        while head != None:
            if head not in visited:
                visited.add(head)
                head = head.next
            else:
                return True
        return False


    # * Solution 2
    # ! Two pointers: Fast and Slow
    def hasCycle2(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast and fast.next and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False



# * Helpers
def buildLinkedList(nodes:list, index: int, pos: int, circleStartNode: ListNode)-> ListNode:
    head = ListNode(nodes[index])
    if index == pos:
        circleStartNode = head
    if index != len(nodes)-1:
        head.next = buildLinkedList(nodes, index+1, pos, circleStartNode)
    else:
        head.next = circleStartNode
    return head


def printLinkedList(head: ListNode):
    visited = set()
    while head and head not in visited:
        print('{} -> '.format(head.val), end='')
        visited.add(head)
        head = head.next
    
    if head:
        print(head.val)
    else:
        print('END')



sol = Solution()
nodes = [3, 2, 0, -4]
pos = 1
head: ListNode = buildLinkedList(nodes, 0, pos, None)
print(head)
print(head.val)
printLinkedList(head)

r1 = sol.hasCycle2(head)
print(r1)

print()
nodes = [1,2]
pos = -1
head: ListNode = buildLinkedList(nodes, 0, pos, None)
print(head)
print(head.val)
printLinkedList(head)

r1 = sol.hasCycle2(head)
print(r1)

print()
