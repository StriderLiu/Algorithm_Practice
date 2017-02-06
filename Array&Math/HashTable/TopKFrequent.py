import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Hash
        hash = {}
        for num in nums:
            if  num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1

        # Min Heap
        h = []
        for key in hash:
            heapq.heappush(h, (-hash[key], key)) # push (-frequncy, key) into heap
        return [heapq.heappop(h)[1] for i in range(k)] # pop k times to assemble the result


nums, k = [1, 1, 1, 2, 2, 3], 2
print(Solution().topKFrequent(nums, k))