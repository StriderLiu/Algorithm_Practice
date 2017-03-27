class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return max(nums)

        # one pass
        first, second, third = float('-inf'), float('-inf'), float('-inf')
        for i in range(n):
            if nums[i] == first or nums[i] == second or nums[i] == third:
                continue

            if nums[i] > first:
                third = second
                second = first
                first = nums[i]
            elif nums[i] > second:
                third = second
                second = nums[i]
            elif nums[i] > third:
                third = nums[i]

        if third == float('-inf'):
            return first
        return third

nums = [2, 2, 8, 1, 0, 3, 2, 4, 5]
print(Solution().thirdMax(nums))