#
# * 111. Minimum Depth of Binary Tree

# * Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root 
# node down to the nearest leaf node.

# * Note: A leaf is a node with no children.

# * Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# * Example 2:

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

 

# * Constraints:

#     The number of nodes in the tree is in the range [0, 105].
#     -1000 <= Node.val <= 1000


#%%
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        queue = []
        queue.append(root)
        depth = 1

        while len(queue) > 0:
            n = len(queue)

            for i in range(n):
                curNode = queue.pop(0)
                # print(curNode.val)

                if curNode.left == None and curNode.right == None:
                    return depth

                if curNode.left != None:
                    queue.append(curNode.left)
                if curNode.right != None:
                    queue.append(curNode.right)
                
            depth += 1




def buildTree(nodes:list)-> TreeNode:
    root=TreeNode(nodes[0])
    i = 1
    while i < len(nodes):
        pass



# * Build sample tree
root = TreeNode(3)
root.left = TreeNode(9)
right1 = TreeNode(20)
root.right = right1
left1 = TreeNode(15)
right1.left = left1
right1.right = TreeNode(7)

sol = Solution()
r1 = sol.minDepth(root)
print(r1)

        
# %%
