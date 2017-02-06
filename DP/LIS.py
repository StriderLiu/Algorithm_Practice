class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n^2) Solution: Dynamic Programming
        # n = len(nums)
        # f = [0] + [1] * n
        # for i in range(1, n + 1):
        #     for j in range(1, i):
        #         if nums[j - 1] < nums[i - 1]:
        #             f[i] = max(f[i], f[j] + 1)
        #
        # return max(f) # remember to select the max from the state array

        # O(nlogn) Solution: Binary Search
        if not nums:
            return 0
        stack = [nums[0]]
        maxLen = 1
        for i in range(1, len(nums)):
            if nums[i] > stack[-1]:
                stack.append(nums[i])
            else:
                index = self.binarySearch(stack, nums[i])
                stack[index] = nums[i]
            maxLen = max(maxLen, len(stack))
        return maxLen

    def binarySearch(self, stack, num):
        left, right = 0, len(stack) - 1
        while left < right:
            mid = int(left + (right - left) / 2)
            if stack[mid] >= num:
                right = mid
            else:
                left = mid + 1
        return left

nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(Solution().lengthOfLIS(nums))