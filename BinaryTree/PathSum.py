# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.helper(root, sum, root.val)

    def helper(self, root, tar, pSum):
        if not root.left and not root.right:
            if tar == pSum:
                return True
            else:
                return False
        left, right = False, False
        if root.left:
            left = self.helper(root.left, tar, pSum + root.left.val)
        if root.right:
            right = self.helper(root.right, tar, pSum + root.right.val)
        if left or right:
            return True
        return False