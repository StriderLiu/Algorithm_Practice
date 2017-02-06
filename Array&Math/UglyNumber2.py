import heapq

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [0, 1]
        m1, m2, m3 = 1, 1, 1
         
        if (n < len(ugly)):
            return ugly[n]
         
        while n >= len(ugly):
            next = min([ugly[m1] * 2, ugly[m2] * 3, ugly[m3] * 5])
            ugly.append(next)
             
            if ugly[m1] * 2 == next:
                m1 += 1
            if ugly[m2] * 3 == next:
                m2 += 1
            if ugly[m3] * 5 == next:
                m3 += 1
             
        return ugly[n]
    
#         h = [(1, 1)]
#         
#         for _ in range(n):
#             val, fact = heapq.heappop(h)
#             for x in 2, 3, 5:
#                 if fact <= x:
#                     heapq.heappush(h, (val * x, x))
#         
#         return val
    
print(Solution().nthUglyNumber(30))
