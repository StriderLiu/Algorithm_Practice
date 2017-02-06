# -*- coding: utf-8 -*-

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
#         # Solution with hash table
#         T = {
#                 0: '',                
#                 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
#                 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
#                 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX',
#                 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 200: 'CC',
#                 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC',
#                 800: 'DCCC', 900: 'CM', 1000: 'M', 2000: 'MM', 3000: 'MMM'
#         }
#         
#         l, res = [], ''
#         while int(num):
#             l.append(num % 10)
#              num = int(num / 10)
#            
#         for i in range(len(l)):
#             res = T[l[i] * (10 ** i)] + res
#          
#         return res
        
        # SOLUTION without hashing!
        # The wisdom of this solution is it uses digit-fetching technology
        # as well as the feature of array which brilliantly avoid hash table
        M = ['', 'M', 'MM', 'MMM']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        return M[int(num / 1000)] + C[int((num % 1000) / 100)] + \
                 X[int((num % 100) / 10)] + I[num%10]
        
print(Solution(). intToRoman(207))