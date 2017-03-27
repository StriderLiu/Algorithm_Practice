# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        self.closest = float('inf')
        self.findClosest(root, target)

        self.index = -1
        self.closestAt = -1
        nums = []
        self.inorder(root, nums)

        j = min(self.closestAt + k - 1, self.index)
        i = j - k + 1
        while j >= self.closestAt and i > 0:
            if abs(nums[i - 1] - target) < abs(nums[j] - target):
                i -= 1
            j -= 1
        return nums[i: i + k]

    def findClosest(self, root, target):
        if not root:
            return
        if abs(self.closest - target) > abs(root.val - target):
            self.closest = root.val

        if root.val > target:
            self.findClosest(root.left, target)
        else:
            self.findClosest(root.right, target)

    def inorder(self, root, nums):
        if not root:
            return
        self.inorder(root.left, nums)
        nums.append(root.val)
        self.index += 1
        if root.val == self.closest:
            self.closestAt = self.index
        self.inorder(root.right, nums)

root = TreeNode(1)
print(Solution().closestKValues(root, 0.00, 1))