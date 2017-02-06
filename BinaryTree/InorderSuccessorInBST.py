# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        succ = p.right
        if succ: # First choice comes from its right and then left to last node
            while succ and succ.left:
                succ = succ.left
        else: # Second choice: find root with minimum value in all roots such that root.val > p.val
            closest = sys.maxsize
            while root and root.val != p.val:
                if p.val < root.val:
                    if root.val < closest:
                        succ = root
                        closest = root.val
                    root = root.left
                elif p.val > root.val:
                    root = root.right
        return succ