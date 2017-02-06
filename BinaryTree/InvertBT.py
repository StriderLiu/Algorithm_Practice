# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        elif root.left is None and root.right is None:
            return root
        elif root.left is None:
            root.left  = root.right
            root.right = None
            
            root.left = self.invertTree(root.left)
        elif root.right is None:
            root.right = root.left
            root.left = None
            
            root.right = self.invertTree(root.right)
        else:
            temp = root.left
            root.left = root.right
            root.right = temp
            
            root.left = self.invertTree(root.left)
            root.right = self.invertTree(root.right)
            
        return root
    
    def inorderTraverse(self, root):
        if root.left is not None:
            self.inorderTraverse(root.left)
        if root is not None:
            print(root.val)
        if root.right is not None:
            self.inorderTraverse(root.right)
    
root = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(7)
node4 = TreeNode(1)
node5 = TreeNode(3)
node6 = TreeNode(6)
node7 = TreeNode(9)
node8 = TreeNode(10)
node9 = TreeNode(5)

root.left = node2
root.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

node4.left = node8

node7.right = node9

obj = Solution()
obj.inorderTraverse(root)
root = obj.invertTree(root)
print()
obj.inorderTraverse(root)