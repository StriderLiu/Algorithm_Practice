class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Recursion solution will cause stack overflow issue
        if not x:
            return 0
        if not n:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        if n % 2:
            return x * pow(x * x, int(n / 2))
        else:
            return pow(x * x, int(n / 2)) # This cannot be written as pow(x, int(n/2))**2
        # It will cause maximum-recursion-level-exceeded error!!!
        # Because this will be extended as pow(x, int(n/2)) * pow(x, int(n/2))
        # which is no longer a tail recursion
#         st, res, m = [], x, n
#         if n < 0:
#             res = 1 / x
#         while abs(m) >= 1:
#             st.append(m)
#             m = int(m / 2)
#             
#         while len(st) > 1:
#             m = st.pop()
#             res **= 2
#             if n > 0:   
#                 if st[-1] > 2 * m:
#                     res *= x
#             else:
#                 if st[-1] < 2 * m:
#                     res /= x          
#                 
#         return res
    
x = 34.00515
n = -3
print(Solution().myPow(x, n))