#
# * 226. Invert Binary Tree
# * Easy

# * Invert a binary tree.

# * Example:

# * Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9

# * Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Trivia:
# This problem was inspired by this original tweet by Max Howell:

#     Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

#%%
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # * Solution 1, Recursive
    def invertTree1(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None

        self.invertTree1(root.left)
        self.invertTree1(root.right)
        root.left, root.right = root.right, root.left
        
        return root


    # * Solution 2, using BFS
    def invertTree2(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        
        queue = [root]

        while queue:
            thisNode = queue.pop(0)
            thisNode.left, thisNode.right = thisNode.right, thisNode.left
            if thisNode.left:
                queue.append(thisNode.left)
            if thisNode.right:
                queue.append(thisNode.right)

        return root

    
    # * Solution 3, using DFS
    def invertTree3(self, root: TreeNode) -> TreeNode:
        if root:
            stack = [root]

            while stack:
                thisNode = stack.pop()
                if thisNode:
                    thisNode.left, thisNode.right = thisNode.right, thisNode.left
                    stack.extend([thisNode.left, thisNode.right])
        
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
        


tree = [4,2,7,1,3,6,9]
root = buildTree(tree)

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
r1 = sol.invertTree1(root)
# printTreeInorder(r1)
printTreeBFS(r1)
