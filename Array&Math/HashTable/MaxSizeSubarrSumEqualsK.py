class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if not n:
            return 0

        hash, curSum, maxLen = {}, 0, 0
        for i in range(n):
            curSum += nums[i]
            if curSum == k:
                maxLen = i + 1
            elif curSum - k in hash:
                maxLen = max(maxLen, i - hash[curSum - k])
            if curSum not in hash:
                hash[curSum] = i
        return maxLen

nums = [3, -1, 1, 2, 0, 1, 0, 2, -2, 4]
print(Solution().maxSubArrayLen(nums, 3))