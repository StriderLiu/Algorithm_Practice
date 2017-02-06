# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        postS, postE, inS, inE = 0, len(postorder) - 1, 0, len(inorder) - 1
        return self.helper(postorder, postS, postE, inorder, inS, inE)
        
    def helper(self, postorder, postS, postE, inorder, inS, inE):
        if postS > postE or inS > inE:
            return None
        val = postorder[postE]
        ind, root = inorder.index(val), TreeNode(val)
        root.left = self.helper(postorder, postS, postS + ind - inS - 1, inorder, inS, ind - 1)
        root.right = self.helper(postorder, postS + ind - inS, postE - 1, inorder, ind + 1, inE)
        return root 
        