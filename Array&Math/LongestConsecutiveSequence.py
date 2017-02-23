class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashSet = set(nums)
        maxLen = 0
        while hashSet:
            cnt = 0
            start = min(hashSet)
            cur = start
            while cur in hashSet:
                cnt += 1
                cur += 1
            maxLen = max(maxLen, cnt)
            hashSet -= set([i for i in range(start, cur)])
        return maxLen