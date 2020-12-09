#
# * 106. Construct Binary Tree from Inorder and Postorder Traversal
# * Medium

# * Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]

# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7

#%%

# * Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # * Solution 1 
    # ! From Q105 solution 2
    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        if inorder:
            index = inorder.index(postorder.pop())
            root = TreeNode(inorder[index])
            # ! NOTE: build root.right FIRST!
            root.right = self.buildTree(inorder[index+1:], postorder)
            root.left = self.buildTree(inorder[0:index], postorder)
            return root





# * Helpers
# ? Build a tree from a list
def buildTree(vals: list)-> TreeNode:

    # * Recursive helper
    def buildNode(index:int)-> TreeNode:
        thisNode = TreeNode()
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
        


# tree = [4,2,7,1,3,6,9]
# root = buildTree(tree)

# * Test Helpers
# print(root)
# print(root.val)
# print(root.left)
# print(root.left.val)
# print(root.right)
# print(root.right.val)
# printTreeInorder(root)
# printTreeBFS(root)

# * Test soluiotns
sol = Solution()
i1 = [9,3,15,20,7]
p1= [9,15,7,20,3]
r1 = sol.buildTree(i1, p1)
printTreeBFS(r1)
