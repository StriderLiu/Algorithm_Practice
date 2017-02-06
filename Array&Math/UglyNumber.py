class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
#         if num <= 0:
#             return False
#         if num == 1:
#             return True
#         
#         while not num % 2:
#             num /= 2
#         while not num % 3:
#             num /= 3
#         while not num % 5:
#             num /= 5
#             
#         for i in range(7, int(num / 2) + 1, 2):
#             if not num % i:
#                 return False
#             
#         return True

# One of the correct solution:
        if num < 1:
            return 0
        while num > 1:
            if not num % 2:
                num /= 2
            
            if not num % 3:
                num /= 3
                
            if not num % 5:
                num /= 5
                
            return False
        
        return True

# The best solution is here:
#         return num > 0 == 30 ** 32 % num

print(Solution().isUgly(214797179))