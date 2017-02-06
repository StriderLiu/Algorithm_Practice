class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        res, level = 0, 0
        while nestedList:
            level += 1
            temp = []
            for elem in nestedList:
                if type(elem) is int:
                    res += elem * level
                if type(elem) is list:
                    for e in elem:
                        temp.append(e)
            nestedList = temp
        return res

nestedList = [[1,1],2,[1,1]]
print(Solution().depthSum(nestedList))