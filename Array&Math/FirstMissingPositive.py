class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                temp = nums[i] # nested indexing swap must use intermediate variable
                nums[i], nums[temp - 1] = nums[temp - 1], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

nums = [2, 1]
print(Solution().firstMissingPositive(nums))