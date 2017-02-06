# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 11:33:17 2016

@author: vincentliu
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        if n <= 1:
            return
        
        # Find the index of the first element that's less than its right neighbour
        for i in range(-1, -n, -1):
            if nums[i] > nums[i - 1]:
                break
        
        # When num[i - 1] exists
        if i == -n + 1 and nums[i] <= nums[i - 1]:
            # Reverse nums[:]
            p, q = int((n - 1) / 2), int(n / 2)
            while p >= 0 and q <= n - 1:
                nums[p], nums[q] = nums[q], nums[p]
                p -= 1
                q += 1
        else:
            for j in range(n + i, n):
                if nums[j] <= nums[i - 1]:
                    j -= 1
                    break
            # Change the header of the sub permutation
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
            
            # Reverse nums[i:]
            p, q = int(((n + i) + (n - 1)) / 2), int(((n + i) + (n - 1) + 1) / 2)
            while p >= n + i and q <= n - 1:
                nums[p], nums[q] = nums[q], nums[p]
                p -= 1
                q += 1

nums = [1, 3, 2]
Solution().nextPermutation(nums)
print(nums)