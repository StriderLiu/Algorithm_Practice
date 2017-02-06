# -*- coding: utf-8 -*-

# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.

# First, the bf solution takes O(n^3) time, but since we can do 2 sum in O(n) time
# it is also possible to achieve a O(n^2) algorithm

# Then, after try a few examples, we can find the PATTERN:
# A 3 Sum of zero means the selected elements must contain one positive integer and one negetive integer or both 0s
# So I come up with an idea that by splitting the array into two parts 
# with negetive values on the left and non-negetive values on the right

# And then start from the first element of each part (denoted as i and j), we can use the hash-table way to locate the third element

# At last, don't forget to handle the special cases
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 3:
            return []
        
        res = []
        i, j = 0, n - 1
        while i < j:
            if nums[i] < 0:
                i += 1
            if nums[j] >= 0:
                j -= 1
            if i < j and nums[i] >= 0 and nums[j] < 0:
                nums[i], nums[j] = nums[j], nums[i]
            
        if nums[i] < 0:
            i += 1        
        split = i
    
        d, cnt0 = {}, 0
        for i in range(n):
            d[-nums[i]] = i
            if not nums[i]:
                cnt0 += 1
        
        for i in range(split):
            for j in range(split, n):
                s = nums[i] + nums[j]
                if s in d.keys() and ((s >= 0 and d[s] > i) or (s <= 0 and d[s] > j)):
                    l = [nums[i], nums[j], nums[d[s]]]
                    l.sort()
                    if l not in res:
                        res.append(l)
        
        if cnt0 >= 3:
            res.append([0, 0, 0])
                    
        return res
        
# nums = [-1, 0, 1, 2, -1, -4]
nums = [0, 0, 0]
# nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
print(Solution().threeSum(nums))