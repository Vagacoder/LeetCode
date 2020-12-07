#
# * 114. Flatten Binary Tree to Linked List
# * Medium

# * Given a binary tree, flatten it to a linked list in-place.

# For example, given the following tree:

#     1
#    / \
#   2   5
#  / \   \
# 3   4   6

# The flattened tree should look like:

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

#%%
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # ! prev TreeNode for Solution 2
    # ! since flatten() has to return Nothing
    def __init__(self):
        self.prev = None


    # * Solution 1, Post-order flatten
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return

        self.flatten(root.left)
        self.flatten(root.right)
        temp = root.right
        root.right = root.left
        root.left=None

        cur: TreeNode = root
        while cur.right != None:
            cur = cur.right
        
        cur.right = temp

    
    # * Solution 2, With a previous
    def flatten2(self, root: TreeNode)-> None:
        if root == None:
            return
        
        self.flatten2(root.right)
        self.flatten2(root.left)
        root.right = self.prev
        root.left = None;
        self.prev = root


    # * Solution 3, Stack
    # ! Smart!
    def flatten3(self, root: TreeNode)-> None:
        if root == None:
            return

        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.right != None:
                stack.append(cur.right)
            if cur.left != None:
                stack.append(cur.left)
            if stack:
                cur.right = stack[-1]
            cur.left = None



# * Helpers
# ? Build a tree from a list
def buildTree(vals: list)-> TreeNode:

    # * Recursive helper
    def buildNode(index:int)-> TreeNode:
        thisNode = TreeNode()
        # ! Modified to exclude None in vals[]
        if vals[index] != None:
            thisNode.val = vals[index]
        else:
            return

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
        

tree = [1,2,5,3,4,None,6]
root = buildTree(tree)

# * Test Helpers
# print(root)
# print(root.val)
# print(root.left)
# print(root.left.val)
# print(root.right)
# print(root.right.val)
# printTreeInorder(root)
printTreeBFS(root)
print()

sol = Solution()
sol.flatten3(root)
printTreeBFS(root)

# %%
