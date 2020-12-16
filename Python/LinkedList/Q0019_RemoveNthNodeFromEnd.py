#
# * 19. Remove Nth Node From End of List
# * Medium

# * Given the head of a linked list, remove the nth node from the end of the list 
# * and return its head.

# Follow up: Could you do this in one pass?

# * Example 1:

# * 1 -> 2 -> 3 -> 4 -> 5
# * 1 -> 2 -> 3 ------> 5

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# * Example 2:
# Input: head = [1], n = 1
# Output: []

# * Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

# * Constraints:
#     The number of nodes in the list is sz.
#     1 <= sz <= 30
#     0 <= Node.val <= 100
#     1 <= n <= sz

#%%

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # * Solution 1
    # ! Two pointers, fast and slow
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = head
        i = 1
        while fast and i<=n:
            fast = fast.next
            i+=1

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return head


    # * Solution 2
    # ! Nth from End = L-N+1th from Begin
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        # * find length
        length = 0;
        cur = head
        while cur:
            length+=1
            cur = cur.next

        print('length',length)

        # * remove (L-n+1)th from Begin
        toRemove = length - n
        i = 0
        # ! MUST use dummy
        dummy = ListNode(float('-inf'))
        dummy.next=head
        cur = dummy
        while i < toRemove:
            cur = cur.next
            i += 1

        print('cur.val', cur.val)

        cur.next = cur.next.next
        # ! Note: head could be removed, must return dummy.next
        return dummy.next


# * Helpers
def buildLinkedList(nodes:list, index: int, )-> ListNode:
    head = ListNode(nodes[index])

    if index != len(nodes)-1:
        head.next = buildLinkedList(nodes, index+1)

    return head


def printLinkedList(head: ListNode):
    while head :
        print('{} -> '.format(head.val), end='')
        head = head.next
    
    print('END')   



sol = Solution()
nodes = [1, 2, 3, 4, 5]
head = buildLinkedList(nodes, 0)
printLinkedList(head)

n1 = 2
r1 = sol.removeNthFromEnd2(head, n1)
printLinkedList(r1)

print()
nodes = [1, 2]
head = buildLinkedList(nodes, 0)
printLinkedList(head)

n1 = 1
r1 = sol.removeNthFromEnd2(head, n1)
printLinkedList(r1)

print()
nodes = [1, 2]
head = buildLinkedList(nodes, 0)
printLinkedList(head)

n1 = 2
r1 = sol.removeNthFromEnd2(head, n1)
printLinkedList(r1)

print()
nodes = [1]
head = buildLinkedList(nodes, 0)
printLinkedList(head)

n1 = 1
r1 = sol.removeNthFromEnd2(head, n1)
printLinkedList(r1)