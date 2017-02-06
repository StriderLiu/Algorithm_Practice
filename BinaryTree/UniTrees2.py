# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []
        return self.dfs(1, n)

    def dfs(self, start, end):
        if end < start:
            return [None]
        if end == start:
            return [TreeNode(start)]

        res = []
        for i in range(start, end + 1):
            lefts = self.dfs(start, i - 1)
            rights = self.dfs(i + 1, end)

            for l in lefts:
                for r in rights:
                    root = TreeNode(i)
                    root.left, root.right = l, r
                    res.append(root)
        return res

print(Solution().generateTrees(3))
