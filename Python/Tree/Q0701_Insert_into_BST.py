#
# * 701. Insert into a Binary Search Tree
# * Medium

# * You are given the root node of a binary search tree (BST) and a value to insert 
# * into the tree. Return the root node of the BST after the insertion. It is 
# * guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long as 
# the tree remains a BST after insertion. You can return any of them.

# * Example 1:

#       4
#      / \
#    2    7
#   / \
# 1    3

#        4
#      /  \
#    2     7
#   / \   /
# 1    3 5

# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]

# * Example 2:

# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]

# Example 3:

# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]

#%%
# * Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # * Solution 1
    # * Recursive
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        def insertHelper(root: TreeNode, val:int)-> TreeNode:
            if not root:
                return TreeNode(val)
            elif val > root.val:
                root.right = insertHelper(root.right, val)
            elif val < root.val:
                root.left = insertHelper(root.left, val)

            return root

        return insertHelper(root, val)



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

nodes = [4,2,7,1,3]
head = buildTree(nodes)
# printTreeInorder(head)
print()
printTreeBFS(head)
print()

v1 = 5
r1 = sol.insertIntoBST(head, v1)
printTreeBFS(r1)
print()

nodes = [40,20,60,10,30,50,70]
head = buildTree(nodes)
v1 = 25
r1 = sol.insertIntoBST(head, v1)
printTreeBFS(r1)
print()