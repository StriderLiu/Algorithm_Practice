class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1 or nums[0] < nums[-1]:
            return nums[0]

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            if nums[start] < nums[end]:
                return nums[start]

            mid = start + (end - start) // 2
            if nums[mid] > nums[start]:
                start = mid
            elif nums[mid] < nums[start]:
                end = mid
            else:
                start += 1

        return nums[end]

# nums = [4, 5, 6, 7, 0, 1, 2]
nums = [1, 4]
print(Solution().findMin(nums))