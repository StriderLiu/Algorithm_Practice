class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1 for i in range(n)]
        left = 1
        for i in range(1, n):
            # res[i] = res[i - 1] * nums[i - 1]
            left *= nums[i - 1]
            res[i] *= left
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res

print(Solution().productExceptSelf([1, 2, 3, 4]))