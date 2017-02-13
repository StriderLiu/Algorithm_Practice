# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, dummy = [], TreeNode(-1) # Because root could be deleted, so we need a dummy node
        dummy.left = root
        while dummy.left:
            curLeaves = []
            self.helper(dummy, curLeaves)
            res.append(curLeaves)
        return res

    def helper(self, root, curLeaves):
        if not root:
            return

        if root.left and not root.left.left and not root.left.right:
            curLeaves.append(root.left.val)
            root.left = None # the only to delete node in tree
        if root.right and not root.right.left and not root.right.right:
            curLeaves.append(root.right.val)
            root.right = None

        self.helper(root.left, curLeaves)
        self.helper(root.right, curLeaves)