# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ResultType(object):
    def __init__(self, isBalanced, maxDep):
        self.isBalanced = isBalanced
        self.maxDep = maxDep


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root).isBalanced

    def helper(self, root):
        if not root:
            return ResultType(True, 0)

        left = self.helper(root.left)
        right = self.helper(root.right)

        if not left.isBalanced or not right.isBalanced:
            return ResultType(False, -1)
        if abs(left.maxDep - right.maxDep) > 1:
            return ResultType(False, -1)
        return ResultType(True, 1 + max(left.maxDep, right.maxDep))
