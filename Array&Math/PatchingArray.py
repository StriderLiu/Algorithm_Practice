import sys

class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
# For this solution, I got a 'Memory Error'
# I guess maybe it is the insertion on large list that cause this problem
# Looking for a better solution
#         i, sum, count = 0, 0, 0
#         
#         for target in range(1, n + 1):
#             if len(nums) == 0:
#                 nums.insert(i, target)
#                 sum += target
#                 count += 1
#                 nums.append(sys.maxsize)
#                 i += 1
#                 
#             elif target > sum:
#                 if target > nums[i]:
#                     i += 1
#                     if i == len(nums) - 1 and nums[i] != sys.maxsize:
#                         nums.append(sys.maxsize)
#                     sum += nums[i]
#                 else:
#                     nums.insert(i, target)
#                     i += 1
#                     sum += target
#                     count += 1   
#             elif target == nums[i]:
#                 if i == len(nums) - 1 and nums[i] != sys.maxsize:
#                     nums.append(sys.maxsize)
#                 sum += target
#                 i += 1
#                 
#         return count

# So I can just find the pattern in this question and record the max value that the current list can reach
# There is no need to actually add the new elements into the list
# The more abstract you consider this problem, the clearer understanding you will get

        i, cnt, maxScope = 0, 0, 0
        
        while maxScope < n:
            if i < len(nums) and nums[i] <= maxScope + 1:
                maxScope += nums[i]
                i += 1
            else:
                maxScope += maxScope + 1
                cnt += 1
                
        return cnt
        
nums = []
n = 8
print(Solution().minPatches(nums, n))