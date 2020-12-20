#
# * 450. Delete Node in a BST
# * Medium

# * Given a root node reference of a BST and a key, delete the node with the given 
# * key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

#     Search for a node to remove.
#     If the node is found, delete the node.

# Follow up: Can you solve it with time complexity O(height of tree)?

# * Example 1:

#         5
#       /  \
#      3    6
#    /  \    \
#   2    4    7

#         5
#       /  \
#      4    6
#    /       \
#   2         7

# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# * Example 2:

# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.

# * Example 3:

# Input: root = [], key = 0
# Output: []

# * Constraints:

#     The number of nodes in the tree is in the range [0, 104].
#     -105 <= Node.val <= 105
#     Each node has a unique value.
#     root is a valid binary search tree.
#     -105 <= key <= 105

#%%

# * Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        if not root:
            return None
        elif key == root.val:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            rightMin = self.getMin(root.right)
            root.right = self.deleteMin(root.right)
            rightMin.left = root.left
            rightMin.right = root.right
            root.left = None
            root.right = None
            return rightMin
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        return root


    # * Helper, find and return min node in a bst
    def getMin(self, root: TreeNode) -> TreeNode:
        while root.left:
            root = root.left
        return root


    # * Helper, delete min node in a bst
    def deleteMin(self, root: TreeNode)-> TreeNode:
        if not root.left:
            return root.right
        else:
            root.left = self.deleteMin(root.left)
        return root




# * Helpers
# ? Build a tree from a list
def buildTree(vals: list)-> TreeNode:

    # * Recursive helper
    def buildNode(index:int)-> TreeNode:
        thisNode = TreeNode()
        # thisNode.val = vals[index]

        # ! Modified to exclude None in vals[]
        if vals[index] != None:
            thisNode.val = vals[index]
        else:
            return None

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
def printTreeInorder(root: TreeNode):
    if root:
        print(root.val)
        printTreeInorder(root.left)
        printTreeInorder(root.right)


# ? Print a tree using BFS
def printTreeBFS(root: TreeNode):
    queue = [root]
    while queue:
        thisNode: TreeNode = queue.pop(0)
        if thisNode:
            print(thisNode.val)
            queue.append(thisNode.left)
            queue.append(thisNode.right)
        else:
            print('None')


sol = Solution()

nodes = [5,3,6,2,4, None ,7]
head = buildTree(nodes)
# printTreeInorder(head)
print()
printTreeBFS(head)
print()

k1 = 3
r1 = sol.deleteNode(head, k1)
printTreeBFS(r1)
print()
