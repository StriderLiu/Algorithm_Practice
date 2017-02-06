# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if q == p:
            return q
        self.lca = root
        self.helper(root, p, q)
        return self.lca

    # return number of nodes in (q, p) find
    # if left find 1 and right find 1: lca = root
    # if root is p or q and left or right returns 1: lca = root
    def helper(self, root, p, q):
        if not root:
            return 0

        found = 0
        if root == q or root == p:
            found += 1

        left, right = self.helper(root.left, p, q), self.helper(root.right, p, q)
        if found and (left == 1 or right == 1):
            self.lca = root
        if left == 1 and right == 1:
            self.lca = root

        found += left + right
        return found