class Solution(object):
	def binarySearch(self, nums, target):
		if not len(nums):
			return -1

		start, end = 0, len(nums) - 1
		while start + 1 < end:
			mid = int(start + (end - start) / 2) # Notice in Python float must be transformed to integer
			if target == nums[mid]:
				end = mid # find the first
			elif target > nums[mid]:
				start = mid
			elif target < nums[mid]:
				end = mid

		if target == nums[start]:
			return start
		if target == nums[end]:
			return end

		return -1 # searching failed

nums = [0, 1, 3, 6, 7, 9, 12, 30]
target = 3
print(Solution().binarySearch(nums, target))