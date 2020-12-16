#
# * 876. Middle of the Linked List
# * Easy

# * Given a non-empty, singly linked list with head node head, return a middle 
# * node of linked list.

# * If there are two middle nodes, return the second middle node.

# * Example 1:

# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

# * Example 2:

# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.

# * Note: The number of nodes in the given list will be between 1 and 100.

#%%

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # * Solution 1
    # ! Two pointers, fast and slow
    def middleNode1(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow


    # * Solution 2
    # ! use memo
    def middleNode2(self, head: ListNode) -> ListNode:
        memo = [head]
        while memo[-1].next:
            memo.append(memo[-1].next)
        return memo[len(memo)//2]


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

r1 = sol.middleNode2(head)
print(r1)
printLinkedList(r1)

nodes = [1, 2, 3, 4, 5, 6]
head = buildLinkedList(nodes, 0)
printLinkedList(head)
r1 = sol.middleNode2(head)
print(r1)
printLinkedList(r1)

# %%
