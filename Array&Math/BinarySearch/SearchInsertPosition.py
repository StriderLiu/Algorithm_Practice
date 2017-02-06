class Solution(object):
    # Be careful with 2 cases:
    # 1. target equals to nums[mid]
    # 2. target is less than the first element or larger than the last element
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if target <= nums[0]:
            return 0
        if target > nums[n-1]:
            return n 
        
        low, high = 0, n - 1 
        while low + 1 < high:
            mid = int(low + (high - low) / 2)
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                high = mid
            if target > nums[mid]:
                low = mid
                
        return high
    
nums = [1, 3]
target = 1
print(Solution().searchInsert(nums, target))