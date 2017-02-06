# -*- coding: utf-8 -*-

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
            
        res = []
        
        self.dfs(nums, res, [], 0)
        
        return res
        
    def dfs(self, nums, res, cur, index):
        if index == len(nums) + 1:
            return 
        
        # For lists with same items but in different orders, 
        # they are treated differently.
        # So sort the list before putting it in
        cur.sort()        
        if cur not in res:
            res.append(cur[:])
            
        for i, elem in enumerate(nums[index:]):
            # It is tricky to handle loop invariant for recursion!
            # index is the primary key and i is the secondary key which helps locate the next primary key
            self.dfs(nums, res, cur + [elem], index + i + 1)
            
print(Solution().subsetsWithDup([4, 4, 1, 4]))