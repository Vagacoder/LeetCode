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
    # ! INorder tranversal
    # ? In inorder tranversal on BST, current node val is always smaller than
    # ? previouos node val. We use self.preval to store val of previous node.
    def isValidBST2(self, root: TreeNode)-> bool:
        
        self.preVal = None

        # * Inorder traversal
        def isValidBstHelper(root: TreeNode) -> bool:
            # * base case 
            if not root:
                return True

            # * left subtree
            isLeftValid = isValidBstHelper(root.left)
            if not isLeftValid:
                return False

            # * this node
            if root.left and root.left.val >= root.val:
                return False
            if root.right and root.right.val <= root.val:
                return False

            if self.preVal != None and self.preVal >= root.val:
                return False
         
            self.preVal = root.val
            
            # * right subtree
            isRightValid = isValidBstHelper(root.right)

            return isRightValid

        
        return isValidBstHelper(root)


    # * Solution 3
    # ! PREorder tranversal with val range
    def isValidBST3(self, root: TreeNode)-> bool:
        def isValidBstHelper(root: TreeNode, minVal: int, maxVal: int):
            # Base case
            if not root:
                return True
            if root.val <= minVal:
                return False
            if root.val >= maxVal:
                return False
            return isValidBstHelper(root.left, minVal, root.val) and isValidBstHelper(root.right, root.val, maxVal)

        return isValidBstHelper(root, float('-inf'), float('inf'))




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

nodes = [2, 1, 3]
head = buildTree(nodes)
# printTreeInorder(head)
print()
printTreeBFS(head)
print()

r1 = sol.isValidBST3(head)
print(r1)
print()

nodes = [5,1,4,None,None,3,6]
head = buildTree(nodes)
# printTreeInorder(head)
print()
printTreeBFS(head)
print()

r1 = sol.isValidBST3(head)
print(r1)
print()

nodes = [4,3,5,None,None,1,6]
head = buildTree(nodes)
# printTreeInorder(head)
print()
printTreeBFS(head)
print()

r1 = sol.isValidBST3(head)
print(r1)
print()

nodes = [1,1]
head = buildTree(nodes)
# printTreeInorder(head)
print()
printTreeBFS(head)
print()

r1 = sol.isValidBST3(head)
print(r1)
print()

nodes = [32,26,47,19,None,None,56,None,27]
head = buildTree(nodes)
# printTreeInorder(head)
print()
printTreeBFS(head)
print()

r1 = sol.isValidBST3(head)
print(r1)
# %%
