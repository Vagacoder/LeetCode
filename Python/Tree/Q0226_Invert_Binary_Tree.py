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
    # * Solution 1
    def invertTree1(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        
        return root


# * Helper
def buildTree(vals: list)-> TreeNode:

    # * Recursive helper
    def buildNode(leftI:int, rightI:int)-> TreeNode:
        pass

    
    root = TreeNode([vals[0]])
    

    return root


sol = Solution()
