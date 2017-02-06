# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, '', res)
        return res

    def dfs(self, root, cur, res):
        if not root:
            return

        if not root.left and not root.right:
            cur += str(root.val)
            res.append(cur)
            return

        cur += str(root.val) + '->'
        self.dfs(root.left, cur, res)
        self.dfs(root.right, cur, res)
