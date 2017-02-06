# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root.left and not root.right:
            return root.val
        self.maxSum = -sys.maxsize
        self.dfs(root)
        return self.maxSum

    def dfs(self, root):
        if not root:
            return -sys.maxsize

        lMax = self.dfs(root.left)
        rMax = self.dfs(root.right)

        curMax = root.val
        if lMax > 0:
            curMax += lMax
        if rMax > 0:
            curMax += rMax
        self.maxSum = max(self.maxSum, curMax)

        toParent = root.val
        if not (lMax < 0 and rMax < 0):
            toParent += max(lMax, rMax)

        return toParent
