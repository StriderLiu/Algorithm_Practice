class Solution(object):
	def isUnique_Bit(self, str):
		# Python int has 32 bit if the value can fit in, else
		# it will automatically upgrade to long (64 bits)
		checker = 0
		for c in str:
			val = ord(c) - ord('a')
			if checker & (1 << val) > 0:
				return False
			checker |= (1 << val)

		return True

if __name__ == '__main__':
	str = 'abcdefgbc'
	print(Solution().isUnique_Bit(str))