class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        if len(secret) is 0:
            return '0A0B'
        bull = 0
        cow = 0
        result = []
        for i in range(10):
            result.append(0)
        
        for i in range(len(secret)):
            x = ord(secret[i]) - 48
            y = ord(guess[i]) - 48
            
            if x == y:
                bull += 1
            else:
                if result[x] < 0:
                    cow += 1
                result[x] += 1
                
                if result[y] > 0:
                    cow += 1
                result[y] -= 1
                
        return str(bull) + 'A' + str(cow) + 'B'
    
if __name__ == '__main__':
    secret = '11231'
    guess = '01113'
    print(Solution().getHint(secret, guess))