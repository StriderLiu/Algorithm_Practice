# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total = 0
        self.dfs(root, 0)
        return self.total

    def dfs(self, root, curSum):
        if not root:
            return

        curSum = curSum * 10 + root.val
        if not root.left and not root.right:
            self.total += curSum

        self.dfs(root.left, curSum)
        self.dfs(root.right, curSum)