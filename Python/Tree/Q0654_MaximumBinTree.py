#
# * 654. Maximum Binary Tree
# * Meidum

# *  Given an integer array with no duplicates. A maximum tree building on this 
# * array is defined as follow:

#     The root is the maximum number in the array.
#     The left subtree is the maximum tree constructed from left part subarray 
#       divided by the maximum number.
#     The right subtree is the maximum tree constructed from right part subarray 
#       divided by the maximum number.

# Construct the maximum tree by the given array and output the root node of this tree.

# * Example 1:

# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:

#       6
#     /   \
#    3     5
#    \    / 
#     2  0   
#      \
#      1

# Note: The size of the given array will be in the range [1,1000].

#%%

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # * Solution 1, Recursive
    def constructMaximumBinaryTree(self, nums: list) -> TreeNode:
        
        def findMaxIndex(nums: list, startI: int, endI: int)-> int:
            return nums.index(max(nums[startI: endI]))

        # print(findMaxIndex(nums, 0, len(nums)))

        def buildMaxBinTree(nums:list, startI: int, endI: int) -> TreeNode:
            if startI >= endI:
                return None

            root = TreeNode()
            maxI = findMaxIndex(nums, startI, endI)
            root.val = nums[maxI]
            root.left = buildMaxBinTree(nums, startI, maxI)
            root.right = buildMaxBinTree(nums, maxI+1, endI)
            return root

        return buildMaxBinTree(nums, 0, len(nums))


    # * Solution 2, Using stack, O(N)
    # ! Awesome !
    def constructMaximumBinaryTree2(self, nums: list) -> TreeNode:
        n = len(nums)
        stack = []

        for i in range(n):
            cur = TreeNode(nums[i])
            while stack and stack[-1].val < nums[i]:
                cur.left = stack.pop()

            if stack:
                stack[-1].right = cur
            
            stack.append(cur)
        
        return stack[0]



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
        


tree = [3,2,1,6,0,5]
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
r1 = sol.constructMaximumBinaryTree2(tree)
printTreeBFS(r1)

# %%
