# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

class Solution(object):
    def checkPerm(self, str1, str2):
        if len(str1) != len(str2):
            return False

        charTable = []
        for i in range(0, 128):
            # O(1), initialization
            charTable.append(0)

        for c in str1:
            # O(n), record the count of each chars in str1
            charTable[ord(c)] += 1

        for c in str2:
            # O(n), kick out each chars of str2
            charTable[ord(c)] -= 1

        for c in str2:
            # O(n), see if those two strings match
            if charTable[ord(c)] != 0:
                return False

        return True

if __name__ == '__main__':
    str1 = 'abdee'
    str2 = 'ebaed'

    checker = Solution()
    print(checker.checkPerm(str1, str2))