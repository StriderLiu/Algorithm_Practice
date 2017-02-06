class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        
        # Always take care of special cases first
        if not preorder:
            return True
        
        if preorder[0] == '#':
            if len(preorder) == 1:
                return True
            else:
                return False
        
        # This pre-processing is very important
        preorder = preorder.split(',')
        # Use stack
        stack = []
        stack.append(2)
        for c in preorder[1:]:
            if not stack:
                return False
            
            stack[-1] -= 1
            if stack[-1] == 0:
                stack.pop()
                
            if c != '#':
                stack.append(2)
                
        if not stack:
            return True
        else:
            return False
            
print(Solution().isValidSerialization('1,2,#,3,4,#,5,#,#,#,#'))