class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pascal = [1]
        for row in range(1, rowIndex + 1):
            pre = 1
            for i in range(1, row):
                cur = pascal[i] + pre
                pre = pascal[i]
                pascal[i] = cur
            pascal.append(1)
        return pascal

print(Solution().getRow(5))