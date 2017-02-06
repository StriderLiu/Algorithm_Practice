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
        if p.val == q.val:
            return p

        self.small, self.large = p, q
        if p.val > q.val:
            self.small, self.large = q, p

        self.res = root
        self.helper(root)
        return self.res

    # 1. small < large < root: go left
    # 2. root < small < large: go right
    # 3. small < root < large: res = root
    # 4. small = root or large = root: res = root
    def helper(self, root):
        if self.small.val < root.val < self.large.val or self.small.val == root.val or self.large.val == root.val:
            self.res = root
            return
        if self.large.val < root.val:
            self.helper(root.left)
        if self.small.val > root.val:
            self.helper(root.right)