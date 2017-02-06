# Greedy version
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        f = [0 for i in range(n)]
        if n == 1:
            return nums[0]
        else:
            f[0] = nums[0]

        maxSum = f[0]
        for i in range(1, n):
            f[i] = max(f[i - 1], 0) + nums[i]
            maxSum = max(maxSum, f[i])
        return maxSum

# import sys
# # Recursion version
# class Solution(object):
#     def __init__(self):
#         self.maxSum = -sys.maxsize
#
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         self.helper(nums)
#         return self.maxSum
#
#     def helper(self, nums):
#         n = len(nums)
#         if n == 1:
#             self.maxSum = nums[0]
#             return nums[0]
#
#         curtMax = max(self.helper(nums[0: n - 1]), 0) + nums[n - 1]
#         self.maxSum = max(self.maxSum, curtMax)
#         return curtMax

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))