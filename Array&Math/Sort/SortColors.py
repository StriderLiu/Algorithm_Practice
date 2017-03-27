class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return

        # # O(n) one pass
        # i, j = 0, n - 1
        # for k in range(n):
        #     if k > j:
        #         break
        #     while nums[k] == 2 and k < j:
        #         nums[k], nums[j] = nums[j], nums[k]
        #         j -= 1
        #     while nums[k] == 0 and k > i:
        #         nums[k], nums[i] = nums[i], nums[k]
        #         i += 1

        n0, n1, n2 = -1, -1, -1
        for curt in nums:
            if curt == 0:
                n2 += 1
                nums[n2] = 2
                n1 += 1
                nums[n1] = 1
                n0 += 1
                nums[n0] = 0
            elif curt == 1:
                n2 += 1
                nums[n2] = 2
                n1 += 1
                nums[n1] = 1
            elif curt == 2:
                n2 += 1
                nums[n2] = 1

nums = [1, 2, 2, 1, 2, 0, 1]
Solution().sortColors(nums)
print(nums)