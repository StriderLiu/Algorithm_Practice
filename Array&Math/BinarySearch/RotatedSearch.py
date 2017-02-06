class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not len(nums):
            return -1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if nums[mid] == target:
                return mid
            if nums[start] == target:
                return start
            if nums[end] ==target:
                return end
            
            if nums[mid] < nums[end]:
                if nums[mid] < target < nums[end]:
                    start = mid
                else:
                    end  = mid
#             elif nums[mid] == nums[end]: # if duplicates exist
#                 end -= 1 # can only get rid of one element not half of the array
#                # worst case becomes O(n)
            else:
                if nums[end] < target < nums[mid]:
                    end = mid
                else:
                    start = mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
            
#         l, r = 0, len(nums) - 1
#         
#         while l + 1 < r:
#             m = int(l + (r - l) / 2)
#             if nums[m] == target:
#                 r = m
#             elif (nums[r] < target and nums[m] < target and nums[m] > nums[l]) or \
#                 (nums[l] > target and nums[m] > target and nums[m] > nums[r]) or \
#                 (nums[l] > target and nums[m] < target):
#                 l = m
#             elif (nums[l] > target and nums[m] > target and nums[m] < nums[r]) or \
#                 (nums[r] < target and nums[m] < target and nums[m] < nums[l]) or \
#                 (nums[r] < target and nums[m] > target):
#                 r = m
#             elif nums[l] <= target and target <= nums[r]:
#                 if target > nums[m]:
#                     l = m
#                 else:
#                     r = m
#         
#         if nums[l] == target:
#             return l
#         if nums[r] == target:
#             return r
#         return -1
    
nums = [5, 1, 3]
target = 3
print(Solution().search(nums, target))