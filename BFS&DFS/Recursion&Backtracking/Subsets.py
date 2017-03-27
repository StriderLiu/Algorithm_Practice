class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, n = [[]], len(nums)
        for i in range(n):
            self.dfs(res, nums, [], i, n)
        return res

    def dfs(self, res, nums, curt, i, n):
        curt.append(nums[i])
        res.append(curt[:])

        for j in range(i + 1, n):
            self.dfs(res, nums, curt[:], j, n)