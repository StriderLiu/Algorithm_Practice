# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(root, sum, [])
        return self.res

    def dfs(self, root, curSum, path):
        if not root:
            return
        if not root.left and not root.right:
            if root.val == curSum:
                path.append(root.val)
                self.res.append(path[:])
            return
        path.append(root.val)
        self.dfs(root.left, curSum - root.val, path[:])
        self.dfs(root.right, curSum - root.val, path[:])