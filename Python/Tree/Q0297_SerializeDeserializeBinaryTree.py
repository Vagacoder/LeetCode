#
# * 297. Serialize and Deserialize Binary Tree
# ! Hard

# * Serialization is the process of converting a data structure or object into a 
# * sequence of bits so that it can be stored in a file or memory buffer, or 
# * transmitted across a network connection link to be reconstructed later in the 
# * same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no 
# restriction on how your serialization/deserialization algorithm should work. 
# You just need to ensure that a binary tree can be serialized to a string and 
# this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes 
# a binary tree. You do not necessarily need to follow this format, so please be 
# creative and come up with different approaches yourself.

# * Example 1:

#        1
#      /  \
#     2   3
#       /  \
#     4     5

# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# * Example 2:
# Input: root = []
# Output: []

# * Example 3:
# Input: root = [1]
# Output: [1]

# * Example 4:
# Input: root = [1,2]
# Output: [1,2]

# * Constraints:
#     The number of nodes in the tree is in the range [0, 104].
#     -1000 <= Node.val <= 1000

#%%

# * Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []

        result = [root.val]

        def serHelper(root: TreeNode):
            if not root:
                return 

            if root.left:
                result.append(root.left.val)
            else:
                result.append('null')
            
            if root.right:
                result.append(root.right.val)
            else:
                result.append('null')

            serHelper(root.left)
            serHelper(root.right)


        serHelper(root)
        return result



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        def buildNode(index:int)-> TreeNode:
            if index >= len(data):
                return None

            thisNode = TreeNode(None)
            # thisNode.val = vals[index]
            # # ! Modified to exclude None in vals[]
            if data[index] != 'null':
                thisNode.val = data[index]
            else:
                return None

            n = len(data)
            leftI = index*2+1
            if leftI < n:
                thisNode.left = buildNode(leftI)
            rightI = index*2+2
            if rightI < n:
                thisNode.right = buildNode(rightI)

            return thisNode

        return buildNode(0)




        

# * Helpers
# ? Build a tree from a list
def buildTree(vals: list)-> TreeNode:

    # * Recursive helper
    def buildNode(index:int)-> TreeNode:
        thisNode = TreeNode(None)
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
        


tree = [1, 2, 3, None, None, 4, 5]
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

# * Test soluiotns
ser = Codec()
serResult = ser.serialize(root)
print(serResult)
print()

deser = Codec()
ans = deser.deserialize(serResult)
print(ans)
printTreeBFS(ans)

# ? Case 2
print('\nCase #2')
tree = [1, 2, 3, None, None, 4, 5, 6, 7]
root = buildTree(tree)
printTreeBFS(root)
print()

ser = Codec()
serResult = ser.serialize(root)
print(serResult)
print()

deser = Codec()
ans = deser.deserialize(serResult)
print(ans)
printTreeBFS(ans)