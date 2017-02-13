# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # O(1) space, use traverse 2 times
        self.res, self.maxCnt = [], 0
        self.curVal, self.curCnt = float('inf'), 0
        self.isMaxSet = False

        # inorder makes sure that equal values are visited continually
        self.inorder(root) # O(n)
        self.isMaxSet = True
        self.curVal, self.curCnt = float('inf'), 0 # reset
        # second inorder traversal puts the val with the maxCnt frequency into the result list
        self.inorder(root) # O(n)

        return self.res

    def handle(self, val):
        if val != self.curVal:
            self.curVal = val
            self.curCnt = 0
        self.curCnt += 1

        if self.curCnt > self.maxCnt:
            self.maxCnt = self.curCnt
        elif self.curCnt == self.maxCnt and self.isMaxSet:
            self.res.append(self.curVal)

    # To further save space, I should use Morris traversal
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.handle(root.val) # O(1)
        self.inorder(root.right)

node1 = TreeNode(1)
print(Solution().findMode(node1))