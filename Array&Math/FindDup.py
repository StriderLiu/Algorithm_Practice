# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.

class Solution(object):
    # # O(NlogN)
    # def findDuplicate(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     low, high = 1, len(nums) - 1
    #     while low < high:
    #         mid = low + int((high - low) / 2)
    #         cnt = 0
    #         for i in nums:
    #             if i <= mid:
    #                 cnt += 1
    #         if cnt <= mid:
    #             low = mid + 1
    #         else:
    #             high = mid
    #     return low

    # O(n)
    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]
        finder = 0
        while finder != slow:
            finder, slow = nums[finder], nums[slow]
        return finder