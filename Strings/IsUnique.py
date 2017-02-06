# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

class Solution(object):
    def isUnique(self, str):
        dict = {}

        for letter in str:
            dict[letter] = 0

        for letter in str:
            dict[letter] += 1

        for letter in str:
            if dict[letter] > 1:
                return False

        return True

if __name__ == '__main__':
    str = 'abcdefg'
    print(Solution().isUnique(str))
