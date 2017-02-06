# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """


root = TreeNode(1)
node1 = TreeNode(2)
root.left = node1
print(Solution().upsideDownBinaryTree(root))