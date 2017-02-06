# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        preStart, preEnd, inStart, inEnd = 0, len(preorder) - 1, 0, len(inorder) - 1
        return self.helper(preorder, preStart, preEnd, inorder, inStart, inEnd)
        
    def helper(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        if preStart > preEnd or inStart > inEnd:
            return None
        val = preorder[preStart]
        ind = inorder.index(val)
        root = TreeNode(val)
        root.left = self.helper(preorder, preStart + 1, preStart + ind - inStart,
                                inorder, inStart, ind - 1)
        root.right = self.helper(preorder, preStart + ind - inStart + 1, preEnd,
                                 inorder, ind + 1, inEnd)
        return root