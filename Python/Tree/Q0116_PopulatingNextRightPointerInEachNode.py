#
# * 116. Populating Next Right Pointers in Each Node
# * Meidum

# * You are given a perfect binary tree where all leaves are on the same level, 
# * and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }

# Populate each next pointer to point to its next right node. If there is no next 
# right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Follow up:

#     You may only use constant extra space.
#     Recursive approach is fine, you may assume implicit stack space does not 
#       count as extra space for this problem.

# * Example 1:

# * Input: root = [1,2,3,4,5,6,7]
# * Input:

#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7

# * Output: [1,#,2,3,#,4,5,6,7,#]
# * Output:

#         1
#       /   \
# !   2  ->  3
#    / \    / \
# ! 4-> 5->6-> 7

# Explanation: Given the above perfect binary tree (Figure A), your function should 
#   populate each next pointer to point to its next right node, just like in Figure 
#   B. The serialized output is in level order as connected by the next pointers, 
#   with '#' signifying the end of each level.

# * Constraints:

#     The number of nodes in the given tree is less than 4096.
#     -1000 <= node.val <= 1000

#%%
# Definition for a Node.
class Node:
    def __init__(self, val: int=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    # * Solution 1
    def connect1(self, root: Node) -> Node:
        if not root:
            return None

        if root.left and root.right:
            root.left.next = root.right
            if root.left.right and root.right.left:
                root.left.right.next = root.right.left
            if root.right  and root.next and root.next and root.next.left:
                root.right.next = root.next.left

            self.connect1(root.left)
            self.connect1(root.right)
        return root


    # * Solution 2
    def connect2(self, root: Node) -> Node:
        if not root:
            return None
        
        def connectTwoNode(node1: Node, node2: Node):
            if not node1 or not node2:
                return
            
            node1.next = node2

            connectTwoNode(node1.left, node1.right)
            connectTwoNode(node2.left, node2.right)
            connectTwoNode(node1.right, node2.left)

        connectTwoNode(root.left, root.right)
        return root




# * Helpers
# ? Build a tree from a list
def buildTree(vals: list)-> Node:

    # * Recursive helper
    def buildNode(index:int)-> Node:
        thisNode = Node()
        thisNode.val = vals[index]

        n = len(vals)
        leftI = index*2+1
        if leftI < n:
            thisNode.left = buildNode(leftI)
        rightI = index*2+2
        if rightI < n:
            thisNode.right = buildNode(rightI)

        return thisNode
    
    return buildNode(0)


# ? Print a tree traversaling in in-order
def printTreeInorder(root: Node):
    if root:
        print(root.val)
        printTreeInorder(root.left)
        printTreeInorder(root.right)


# ? Print a tree using BFS
def printTreeBFS(root: Node):
    queue = [root]
    while queue:
        thisNode: Node = queue.pop(0)
        if thisNode:
            print(thisNode.val)
            if thisNode.next:
                print('=>', thisNode.next.val)
            queue.append(thisNode.left)
            queue.append(thisNode.right)
        



# vals = [1,2,3,4,5,6,7]
vals = [-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13]
root = buildTree(vals)
print('Original Tree:')
printTreeBFS(root)

sol = Solution()
print('\nConnected Tree:')
r1 = sol.connect2(root)
printTreeBFS(r1)
