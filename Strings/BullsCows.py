class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        countA = 0
        countB = 0
        for i in range(len(secret)): # O(n)
            if secret[i] == guess[i]:
                countA += 1
        
        d = {}
        for c in secret: # O(n)
            d[c] = 0
        for c in secret: # O(n)
            d[c] += 1
        for c in guess: # O(n)
            if c in d.keys():
                if d[c] > 0:
                    d[c] -= 1
                    countB += 1
                else:
                    del d[c]
                
        countB -= countA
        return str(countA) + 'A' + str(countB) + 'B'

if __name__ == '__main__':
    secret = '1121'
    guess = '0113'
    print(Solution().getHint(secret, guess))