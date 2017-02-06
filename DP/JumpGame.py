class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # O(n) Solution: Greedy
        reachable = 0
        for i in range(len(nums)):
            if reachable < i: return False
            reachable = max(reachable, i + nums[i])
        return True

        # O(n^2) Solution: DP
        # n = len(nums)
        # if not n:
        #     return True
        #
        # f = [True] + [False] * (n - 1)
        # for i in range(1, n):
        #     for j in range(i):
        #         f[i] = f[i] or (f[j] and (i - j <= nums[j]))
        #         if f[i]: break
        # return f[n - 1]