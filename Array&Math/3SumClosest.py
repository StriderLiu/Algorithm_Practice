# -*- coding: utf-8 -*-

# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.
# For example, given array S = {-1 2 1 -4}, and target = 1.
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        
        res = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            tar, j, k = target - nums[i], i + 1, n - 1
            curCls = nums[j] + nums[k]
            
            while j < k:
                tmp = nums[j] + nums[k]
                
                if abs(tmp - tar) < abs(curCls - tar):
                    curCls = tmp
                if tmp < tar:
                    j += 1
                elif tmp > tar:
                    k -= 1
                else:
                    return target
                    
            if abs(curCls + nums[i] - target) < abs(res - target):
                res = curCls + nums[i]
                
        return res

# nums = [2, 1, -2, 3, -3, 4, -5, 11]
nums = [0, -4, 1, -5]
target = 0
print(Solution().threeSumClosest(nums, target))