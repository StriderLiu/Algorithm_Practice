#!/usr/bin/env python
import sys # Do not forget this

class StackWithMin (list): # The base class is just "list"
	#minStack = []

	def __init__ (self):
		self.minStack = []

	def push(self, value): # Do not forget the "self" argument
		if value <= self.min(): # Do not forget to use "self" to call other method in the same class
			self.minStack.append(value) # Global attributes should be refered by class name
		super().append(value) # Use super() instead of super

	def pop(self): # No indication for return type
		value = super().pop()
		if value is self.min():
			self.minStack.pop()
		return value

	def min(self):
		if len(self.minStack) is 0:
			return sys.maxsize
		else:
			return self.minStack[-1] # The most Pyhonic way to refer the last element in the list

if __name__ == '__main__':
	stack = StackWithMin()
	stack.push(5)
	print(stack)
	print(stack.min())
	stack.push(6)
	print(stack)
	print(stack.min())
	stack.push(3)
	print(stack)
	print(stack.min())
	stack.push(7)
	print(stack)
	print(stack.min())
	stack.pop()
	print(stack)
	print(stack.min())
	stack.pop()
	print(stack)
	print(stack.min())	