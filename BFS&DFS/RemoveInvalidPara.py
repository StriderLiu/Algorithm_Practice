class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return ['']
        if self.isValid(s):
            return [s]
        res, toCheck = set(), set([s])
        while '' not in toCheck:
            tmp = set()
            for curt in toCheck:
                for i in range(len(curt)):
                    next = curt[: i] + curt[i + 1:]
                    if self.isValid(next):
                        res.add(next)
                    tmp.add(next)
            if res:
                return list(res)
            toCheck = tmp

        return list(res)

    def isValid(self, s):
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            if c == ')':
                if not cnt:
                    return False
                cnt -= 1
        return cnt == 0

print(Solution().removeInvalidParentheses("n"))