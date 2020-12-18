#
# * 98. Validate Binary Search Tree
# * Medium

# * Given the root of a binary tree, determine if it is a valid binary search 
# * tree (BST).

# * A valid BST is defined as follows:

#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.


# * Example 1:

#       2
#      / \
#    1    3

# Input: root = [2,1,3]
# Output: true

# * Example 2:

#       5
#      / \
#    1    4
#        / \
#      3    6

# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# * Constraints:

#     The number of nodes in the tree is in the range [1, 104].
#     -231 <= Node.val <= 231 - 1

#%%

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # * Solution 1
    # TODO
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left and root.left.val > root.val:
            return False
        if root.right and root.right.val < root.val:
            return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)


    # * Solution 2
    # ! Preoder tranversal
    def isValidBST2(self, root: TreeNode)-> bool:
        
        # * Preorder traversal
        def isValidBstHelper(root: TreeNode, preVal: int) -> bool:
            # * base case 
            if not root:
                return True

            # * left subtree
            isLeftValid = isValidBstHelper(root.left, preVal)
            if not isLeftValid:
                return False

            # * this node
            if root.left and root.left.val >= root.val:
                return False
            if root.right and root.right.val <= root.val:
                return False

            if preVal != None and preVal >= root.val:
                return False
         
            preVal = root.val
            
            # * right subtree
            isRightValid = isValidBstHelper(root.right, preVal)

            return isRightValid

        preVal = None
        return isValidBstHelper(root, preVal)



# * Helpers
# ? Build a tree from a list
def buildTree(vals: list)-> TreeNode:

    # * Recursive helper
    def buildChildNode(root: TreeNode, vals:list):
        if len(vals) > 0:
            leftVal = vals.pop(0)
            if leftVal:
                root.left = TreeNode(leftVal)
        if len(vals) > 0:
            rightVal = vals.pop(0)
            if rightVal:
                root.right = TreeNode(rightVal)

        if root.left:
            buildChildNode(root.left, vals)
        if root.right:
            buildChildNode(root.right, vals)


    nodes = vals.copy()
    root = TreeNode(nodes.pop(0))
    buildChildNode(root, nodes)
    return root


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


sol = Solution()

nodes = [2, 1, 3]
head = buildTree(nodes)
printTreeInorder(head)
print()
printTreeBFS(head)
print()

r1 = sol.isValidBST2(head)
print(r1)
print()

nodes = [5,1,4,None,None,3,6]
head = buildTree(nodes)
printTreeInorder(head)
print()
printTreeBFS(head)
print()

r1 = sol.isValidBST2(head)
print(r1)
print()

nodes = [4,3,5,None,None,1,6]
head = buildTree(nodes)
printTreeInorder(head)
print()
printTreeBFS(head)
print()

r1 = sol.isValidBST2(head)
print(r1)
print()

nodes = [1,1]
head = buildTree(nodes)
printTreeInorder(head)
print()
printTreeBFS(head)
print()

r1 = sol.isValidBST2(head)
print(r1)
print()

nodes = [32,26,47,19,None,None,56,None,27]
head = buildTree(nodes)
printTreeInorder(head)
print()
printTreeBFS(head)
print()

r1 = sol.isValidBST2(head)
print(r1)
# %%
