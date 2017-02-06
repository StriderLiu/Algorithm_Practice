class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1 or nums[0] < nums[-1]:
            return nums[0]

        start, end = 0, n - 1
        while start + 1 < end:
            mid = start + int((end - start) / 2)
            if nums[mid] > nums[start]:
                start = mid
            else:
                end = mid
        return nums[end]