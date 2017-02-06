class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        val = x
        if x < 0:
            val *= -1
            
        stack = []
        while val / 10 >= 1:
            stack.append(val % 10)
            val = int(val / 10)
        else:
            stack.append(val)
        
        i, rev = 0, 0
        while len(stack):
            dig = stack.pop()
            rev += dig * (10 ** i)
            i += 1
            
        # If rev is bigger than maximum 32-bits integer, retrun 0
        if rev > 2147483647:
            return 0
        
        if x < 0:
            rev *= -1
        
        return rev

# Should consider some special cases as below
# What if the reverse number overflow?
print(Solution().reverse(10100))