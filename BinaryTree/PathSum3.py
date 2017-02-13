# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# The path does not need to start or end at the root or a leaf,
# but it must go downwards (traveling only from parent nodes to child nodes)
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        preSum, self.cnt = {0: 1}, 0
        self.helper(root, 0, sum, preSum)
        return self.cnt

    # use prefix to help calculate the sum of a intermediate sequence
    def helper(self, root, curSum, target, preSum):
        if not root:
            return

        curSum += root.val
        if curSum - target in preSum:
            self.cnt += preSum[curSum - target]

        if curSum not in preSum:
            preSum[curSum] = 1
        else:
            preSum[curSum] += 1

        self.helper(root.left, curSum, target, preSum)
        self.helper(root.right, curSum, target, preSum)
        preSum[curSum] -= 1 # this is used to differientiate seperate paths