# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.prev, self.first, self.second = TreeNode(-sys.maxsize), None, None
        self.dfs(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def dfs(self, curt):
        if not curt:
            return

        self.dfs(curt.left)

        if not self.first and self.prev.val >= curt.val:
            self.first = self.prev
        if self.first and self.prev.val >= curt.val:
            self.second = curt
        self.prev = curt

        self.dfs(curt.right)

root = TreeNode(0)
node1 = TreeNode(1)
root.left = node1
Solution().recoverTree(root)