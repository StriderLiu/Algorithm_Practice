class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        hash = {}
        for ch in s:
            if ch not in hash:
                hash[ch] = 1
            else:
                hash[ch] += 1

        import heapq as h
        heap = []
        for ch in hash:
            h.heappush(heap, (-hash[ch], ch))
            res = ''
        while heap:
            [freq, ch] = h.heappop(heap)
            res += ch * (-freq)
        return res

print(Solution().frequencySort('tree'))