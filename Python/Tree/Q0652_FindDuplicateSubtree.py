#
# * 652. Find Duplicate Subtrees
# * Medium

# * Given the root of a binary tree, return all duplicate subtrees.

# For each kind of duplicate subtrees, you only need to return the root node of any one of them.

# Two trees are duplicate if they have the same structure with the same node values.

# * Example 1:
# Input: root = [1,2,3,4,null,2,4,null,null,4]

#        1
#       / \
#      2   3
#    /   /  \
#   4   2    4
#      /
#     4

# Output: [[2,4],[4]]


# * Example 2:
# Input: root = [2,1,1]

#    2
#   / \
#  1   1

# Output: [[1]]


# * Example 3:
# Input: root = [2,2,2,3,null,3,null]

#        2
#      /  \
#     2   2
#    /   /
#   3   3

# Output: [[2,3],[3]]


# * Constraints:

#     The number of the nodes in the tree will be in the range [1, 10^4]
#     -200 <= Node.val <= 200

#%%

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # * Solution 1, 
    def findDuplicateSubtrees(self, root: TreeNode) -> list:
        allSubTrees = {}
        # * return a list ot TreeNode
        result = []

        # * Recursive helper
        def traversalSubTree(root: TreeNode)-> str:
            if root == None:
                return 'None'

            leftStr = traversalSubTree(root.left)
            rightStr = traversalSubTree(root.right)
            rootStr = leftStr + ',' + rightStr + ',' + str(root.val)

            if rootStr in allSubTrees:
                if allSubTrees[rootStr] == 1:
                    result.append(root)
                allSubTrees[rootStr] +=1
            else:
                allSubTrees[rootStr] = 1

            return rootStr

        traversalSubTree(root)
        return result


    # * Solution 2, DFS, from LeetCode Solution
    # ? Acutally same as Solution 1, better code
    def findDuplicateSubtrees2(self, root: TreeNode) -> list:
        import collections
        count = collections.Counter()
        result = []

        def traversalSubTree(root: TreeNode)-> str:
            if not root:
                return '#';
            serial = '{},{},{}'.format(root.val, traversalSubTree(root.left), traversalSubTree(root.right))
            count[serial] +=1
            
            if count[serial] == 2:
                result.append(root)

            return serial
        
        traversalSubTree(root)
        return result


# * Helpers
# ? Build a tree from a list
def buildTree(vals: list)-> TreeNode:

    # * Recursive helper
    def buildNode(index:int)-> TreeNode:
        thisNode = TreeNode()
        # thisNode.val = vals[index]

        # # ! Modified to exclude None in vals[]
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
        


# * tree fro problem
# tree = [1, 2, 3, 4, None, 2, 4, None, None, 4]
# * complete tree as above
tree = [1, 2, 3, 4, None, 2, 4, None, None, None, None, 4, None, None, None]
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
r1 = sol.findDuplicateSubtrees(root)
print(r1)
print('length of result:', len(r1))
for r in r1:
    print(r.val)

# %%
