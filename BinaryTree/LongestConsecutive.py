# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.maxLen = 0
        self.dfs(root, 0, root.val)
        return self.maxLen

    def dfs(self, root, curt, shouldBe):
        if not root:
            return
        if root.val == shouldBe:
            curt += 1
        else:
            curt = 1
        self.maxLen = max(self.maxLen, curt)
        self.dfs(root.left, curt, root.val + 1)
        self.dfs(root.right, curt, root.val + 1)

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.right = node3
node3.left = node2
node3.right = node4
node4.right = node5

Solution().longestConsecutive(node1)