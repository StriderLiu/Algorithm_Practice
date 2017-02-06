# Given an integer n, count how many structurally unique BST's (binary search trees) that store values 1...n.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.cnt = 0
        self.isUni(root)
        return self.cnt

    def isUni(self, root):
        if not root.left and not root.right:
            self.cnt += 1
            return True
        if root.left:
            leftUni = self.isUni(root.left)
        if root.right:
            rightUni = self.isUni(root.right)

        if not root.left:
            if rightUni and root.val == root.right.val:
                self.cnt += 1
                return True
            else:
                return False
        if not root.right:
            if leftUni and root.val == root.left.val:
                self.cnt += 1
                return True
            else:
                return False
        if leftUni and rightUni and root.val == root.left.val and root.val == root.right.val:
            self.cnt += 1
            return True
        return False

root = TreeNode(5)
node1 = TreeNode(1)
node2 = TreeNode(5)
node3 = TreeNode(5)
node4 = TreeNode(5)
node5 = TreeNode(5)
node6 = TreeNode(5)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.right = node5

print(Solution().countUnivalSubtrees(root))
