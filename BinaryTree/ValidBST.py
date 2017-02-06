# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import sys

# class Solution(object):
#     # Traversal Solution, need a global variable
#     def __init__(self):
#         self.isValid = True
#     
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         MAX, MIN = sys.maxsize, -sys.maxsize
#         self.helper(root, MIN, MAX)
#         return self.isValid
#         
#     def helper(self, root, lower, upper):
#         if not root:
#             return 
#         if root.val <=lower or root.val >= upper:
#             self.isValid = False
#             return
#         if root.left:
#             self.helper(root.left, lower, root.val)
#         if root.right:
#             self.helper(root.right, root.val, upper)

class Solution(object):
    # Divide & Conquer Solution
    def isValidBST(self, root):
        MAX, MIN = sys.maxsize, -sys.maxsize
        return self.helper(root, MIN, MAX)
    
    def helper(self, root, lower, upper):
        if not root:
            return True
        if root.val <= lower or root.val >= upper:
            return False
        
        lValid, rValid = True, True
        if root.left:
            lValid = self.helper(root.left, lower, root.val)
        if root.right:
            rValid = self.helper(root.right, root.val, upper)
                
        if lValid and rValid:
            return True
        return False

root = TreeNode(1)
node1 = TreeNode(2)
root.left = node1
print(Solution().isValidBST(root))