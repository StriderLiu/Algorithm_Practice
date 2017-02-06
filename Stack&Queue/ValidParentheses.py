class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        
        tmp = []
        l = len(s)
        for c in s:
            if c in ['(', '[', '{']:
                tmp.append(c)
                l -= 1
                
            elif (c == ')' and len(tmp) and tmp[-1] == '(') or \
                (c == ']' and len(tmp) and tmp[-1] == '[') or \
                (c == '}' and len(tmp) and tmp[-1] == '{'):
                tmp.pop()
                l -= 1
                
        if  not len(tmp) and not l:
            return True
        return False

print(Solution().isValid('()[]{([])}'))
# Be careful with some special cases
# ']]'
# '()]'