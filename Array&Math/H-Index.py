class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True)
        
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i
        
        return i + 1
    
citations = [8, 8, 8, 8, 8]
print(Solution().hIndex(citations))