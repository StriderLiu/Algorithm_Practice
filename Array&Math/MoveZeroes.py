class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, count = 0, 0
        while i < len(nums):
        	if nums[i] == 0:
        		count += 1
        		del nums[i]
        	else:
        		i += 1

        for i in range(count):
        	nums.append(0)

nums = [0, 0, 1, 3, 0, 0, 12]
Solution().moveZeroes(nums)
print(nums)
