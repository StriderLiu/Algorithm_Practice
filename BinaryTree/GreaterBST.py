# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root, 0)
        return root

    def helper(self, root, parSum):
        if not root:
            return 0

        rSum = self.helper(root.right, parSum)
        old = root.val
        root.val += rSum + parSum
        lSum = self.helper(root.left, root.val)

        return old + lSum + rSum