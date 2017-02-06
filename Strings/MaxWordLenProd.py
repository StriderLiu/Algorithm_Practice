class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) == 0 or len(words) == 1:
            return 0
        
        d = {}
        for w in sorted(words, key=len): # pick the word in the order of the length
            mask = 0
            for c in set(w): # only consider the non-duplicate letters
                mask |= (1 << (ord(c) - 97))
            # If they have the same mask, I will have the word
            # with max length at the end
            d[mask] = len(w)
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])

# Better implementation, with bit manipulation matching two strings can be done in O(1) time      
#         max_len = 0
#         bits = []
#         lens = []
#         
#         for str in words:
#             bit = 0
#             for c in str:
#                 bit |= (1 << (ord(c) - ord('a')))
#             bits.append(bit)
#             lens.append(len(str))
#             
#         for i in range(len(bits)):
#             for j in range(len(bits)):
#                 if bits[i] & bits[j] == 0:
#                     max_len = max(max_len, lens[i] * lens[j])
#         return max_len
                    
# Slow implementation    
#         max_len = 0
#         
#         for i, str1 in enumerate(words):
#             num = 0
#             for c in str1:      
#                 num |= (1 << (ord(c) - ord('a')))
#             
#             for str2 in words[(i+1):]:
#                 dup = False
#                 for c in str2:
#                     bit = num & (1 << (ord(c) - ord('a')))
#                     if bit is not 0:
#                         dup = True
#                         break
#                 
#                 if dup is False and len(str1) * len(str2) > max_len:
#                     max_len = len(str1) * len(str2)
        
#         return max_len
    
words = ["abcw", 'abbccw', "baz", "foo", "bar", "xtfn", "abcdef"]
#words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
#words = ["a", "aa", "aaa", "aaaa"]
#
print(Solution().maxProduct(words))