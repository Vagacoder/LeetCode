#
# * 105. Construct Binary Tree from Preorder and Inorder Traversal
# * Medium

# * Given preorder and inorder traversal of a tree, construct the binary tree.

# * Note: You may assume that duplicates do not exist in the tree.

# * For example, given

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]

# * Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7

#%%

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # * Solution 1, 
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        
        def buildTreeHelper(preorder:list, preLeft:int, preRight:int, 
                            inorder: list, inLeft: int, inRight: int)-> TreeNode:

            if preLeft > preRight or inLeft > inRight:
                return None

            root: TreeNode = TreeNode(preorder[preLeft])
            rootIndexIn = inorder.index(root.val, inLeft, inRight+1)
            leftSize = rootIndexIn - inLeft
            rightSize = inRight - rootIndexIn

            root.left = buildTreeHelper(preorder, preLeft+1, preLeft+leftSize, 
                                        inorder, inLeft, rootIndexIn-1)
            root.right = buildTreeHelper(preorder, preLeft+leftSize+1, preRight, 
                                        inorder, rootIndexIn+1, inRight)

            return root

        return buildTreeHelper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)

    
    # * Solution 2, 
    # ! Short and concise!
    def buildTree2(self, preorder: list, inorder: list) -> TreeNode:
        if inorder:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree2(preorder, inorder[0:index])
            root.right = self.buildTree2(preorder, inorder[index+1:])
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
p1= [3,9,20,15,7]
i1 = [9,3,15,20,7]
r1 = sol.buildTree(p1, i1)
printTreeBFS(r1)

# %%
