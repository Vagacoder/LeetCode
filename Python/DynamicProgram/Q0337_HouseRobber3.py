#
# * 337. House Robber 3
# * Medium

# * The thief has found himself a new place for his thievery again. There is only 
# * one entrance to this area, called the "root." Besides the root, each house 
# * has one and only one parent house. After a tour, the smart thief realized that 
# * "all houses in this place forms a binary tree". It will automatically contact 
# * the police if two directly-linked houses were broken into on the same night.

# Determine the maximum amount of money the thief can rob tonight without alerting the police.

# * Example 1:

# Input: [3,2,3,null,3,null,1]

#      3
#     / \
#    2   3
#     \   \ 
#      3   1

# Output: 7 
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

# * Example 2:

# Input: [3,4,5,1,3,null,1]

#      3
#     / \
#    4   5
#   / \   \ 
#  1   3   1

# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

#%%

# * Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # * Solution 1
    def rob1(self, root: TreeNode) -> int:

        memo = {}

        def robRecursive(root: TreeNode)-> self:
            if root == None:
                return 0
            if root in memo:
                return memo[root]
            
            # * case of rob root
            robLeftSide = 0
            robRightSide = 0
            if root.left != None:
                robLeftSide = robRecursive(root.left.left) + robRecursive(root.left.right)
            if root.right != None:
                robRightSide = robRecursive(root.right.left) + robRecursive(root.right.right)
            robRoot = root.val + robLeftSide + robRightSide

            # * case of not rob root
            notRobRoot = robRecursive(root.left) + robRecursive(root.right)

            result = max(robRoot, notRobRoot)
            memo[root] = result
            return result
        

        return robRecursive(root)


    # * Solution 2, Dynamic Programming from Leetcode solution
    def rob2(self, root: TreeNode) -> int:
        if not root:
            return 0
            
        # * reform tree into array-based tree, which is dp
        tree = []
        graph = {-1: []}
        index = -1
        queue = [(root, -1)]
        
        while queue:
            node, parent_index = queue.pop(0)
            if node:
                index += 1
                tree.append(node.val)
                graph[index] = []
                graph[parent_index].append(index)
                queue.append((node.left, index))
                queue.append((node.right, index))

        # represent the maximum start by node i with robbing i
        dp_rob = [0] * (index+1)

        # represent the maximum start by node i without robbing i
        dp_not_rob = [0] * (index+1)

        for i in reversed(range(index+1)):
            if not graph[i]:  # if is leaf
                dp_rob[i] = tree[i]
                dp_not_rob[i] = 0
            else:
                dp_rob[i] = tree[i] + sum(dp_not_rob[child]
                                          for child in graph[i])
                dp_not_rob[i] = sum(max(dp_rob[child], dp_not_rob[child])
                                    for child in graph[i])

        return max(dp_rob[0], dp_not_rob[0])




def buildTree(nodes: list)-> TreeNode:
    root = TreeNode(nodes[0])



sol = Solution()
node1 = [3, 2, 3, None, 3, None, 1]
root = buildTree(node1)
r1 = sol.rob1(root)
print(r1)
