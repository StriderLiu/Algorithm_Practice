# -*- coding: utf-8 -*-

class Solution(object):
#     def __init__(self):
#         self.calculated = {}
    
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n , res= len(nums), []
        
        if not n or n < 4:
            return res
        
        nums.sort()
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]: continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target: break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target: continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target: break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target: continue
                
                left, right = j + 1, n - 1
                while left < right:
                    sum = nums[left] + nums[right] + nums[i] + nums[j]
                    if sum < target: 
                        left += 1
                    elif sum > target: 
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1
                        right -= 1
                        while nums[right] == nums[right + 1] and left < right:
                            right -= 1    

#         self.window(res, nums, target, i, j)
        
        return res
        
#     def window(self, res, nums, target, i, j):       
#         if i > j - 3:
#             return
#             
#         sum1 = nums[i] + nums[j]
#         lo = i + 1
#         hi = j - 1
#             
#         while lo < hi:
#             sum2 = nums[lo] + nums[hi]
#             if sum2 > target - sum1:
#                 hi -= 1
#             elif sum2 < target - sum1:
#                 lo += 1
#             else:
#                 tmp = [nums[i], nums[lo], nums[hi], nums[j]]
#                 if tmp not in res:                
#                     res.append(tmp)
#                 self.calculated[(i, j)] = True
#                 lo += 1
#                 hi -= 1
#                     
#         if (i, j - 1) not in self.calculated.keys():
#             self.window(res, nums, target, i, j - 1)
#         if (i + 1, j) not in self.calculated.keys():
#             self.window(res, nums, target, i + 1, j)

# nums = [-3,-1,0,2,4,5]
# target = 2
# nums = [1, 0, -1, 0, -2, 2]
# target = 0
nums = [-5,-4,-3,-2,-1,0,0,1,2,3,4,5]
target = 0
print(Solution().fourSum(nums, target))