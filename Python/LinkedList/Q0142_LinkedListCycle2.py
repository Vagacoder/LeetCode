#
# * 142. Linked List Cycle 2
# * Medium

# * Given a linked list, return the node where the cycle begins. If there is no 
# * cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be 
# reached again by continuously following the next pointer. Internally, pos is 
# used to denote the index of the node that tail's next pointer is connected to. 
# Note that pos is not passed as a parameter.

# Notice that you should not modify the linked list.

# Example 1:

# * 3 -> 2 -> 0 -> 4
# *      |         |
# *      ----------

# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# * Example 2:

# * 1 -> 2
# * |    |
# * -----

# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.

# * Constraints:

#     The number of the nodes in the list is in the range [0, 104].
#     -105 <= Node.val <= 105
#     pos is -1 or a valid index in the linked-list.

#%%
# * Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # * Solution 1
    # ! Hash memo
    def detectCycle(self, head: ListNode) -> ListNode:
        visited =set()
        while head != None:
            if head not in visited:
                visited.add(head)
                head = head.next
            else:
                return head

        return None


    # * Solution 2
    # ! Two pointers: fast and slow
    def detectCycle2(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
            if fast == slow:
                break

        if fast == None:
            return None

        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow



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

r1 = sol.detectCycle2(head)
print(r1)
print(r1.val)

print()
nodes = [1]
pos = -1
head: ListNode = buildLinkedList(nodes, 0, pos, None)
print(head)
print(head.val)
printLinkedList(head)

r1 = sol.detectCycle2(head)
print(r1)
if r1:
    print(r1.val)

print()