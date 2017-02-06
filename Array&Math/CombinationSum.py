class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        
        res = []
        line = []
        self.dfs(candidates, target, res, line) # send reference, because res will be used as return value
        return res
    
    def dfs(self, candidates, target, res, line):
        if target == 0:
            res.append([x for x in line]) # In default, the reference of 'line' will be sent to function. So it must be modified
            return
        # for with a recursion_backtracking inside is the principle of DFS
        for i, x in enumerate(candidates):
            if x > target: # foresee that the target will be exceeded
                return
            
            line.append(x)
            self.dfs(candidates[i:], target - x, res, line) # only check the nodes with value not less than current one, this ensures the 'line' is unique 
            line.pop() # give space in order to try the next element
                
target = 7
candidates = [2, 3, 6, 7]
print(Solution().combinationSum(candidates, target))