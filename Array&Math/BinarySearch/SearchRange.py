class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        low, high, first, last = 0, n-1, -1, -1
        
        # find first
        while low + 1 < high:
            mid = int(low + (high - low) / 2)
            if target <= nums[mid]:
                high = mid
            if target > nums[mid]:
                low = mid
        if nums[low] == target:
            first = low
        elif nums[high] == target:
            first = high
        
        # find last
        low, high = 0, n-1
        while low + 1 < high:
            mid = int(low + (high - low) / 2)
            if target >= nums[mid]:
                low = mid
            if target < nums[mid]:
                high = mid
        if target == nums[high]:
            last = high
        elif target == nums[low]:
            last = low
        
        return [first, last]