#
# * 700. Search in a Binary Search Tree
# * Easy

# * Given the root node of a binary search tree (BST) and a value. You need to 
# * find the node in the BST that the node's value equals the given value. Return 
# * the subtree rooted with that node. If such node doesn't exist, you should 
# * return NULL.

# * For example, 

# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3

# And the value to search: 2

# You should return this subtree:

#       2     
#      / \   
#     1   3

# In the example above, if we want to search the value 5, since there is no node 
# with value 5, we should return NULL.

# Note that an empty tree is represented by NULL, therefore you would see the 
# expected output (serialized tree format) as [], not null.

#%%
# * Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # * Solution 1
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        elif root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)



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

r1 = sol.searchBST(head, 2)
printTreeBFS(r1)

# %%
