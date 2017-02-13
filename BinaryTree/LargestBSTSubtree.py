# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.maxSize = 0
        self.traverse(root)
        return self.maxSize

    def traverse(self, root):
        if not root:
            return (0, float('inf'), float('-inf'))

        (sizeL, lowerL, upperL) = self.traverse(root.left)
        (sizeR, lowerR, upperR) = self.traverse(root.right)

        if sizeL == -1 or sizeR == -1 or (root.val <= upperL) or (root.val >= lowerR):
            return (-1, 0, 0)

        size = sizeL + sizeR + 1
        lower = min(root.val, lowerL)
        upper = max(root.val, upperR)

        self.maxSize = max(self.maxSize, size)
        return (size, lower, upper)
