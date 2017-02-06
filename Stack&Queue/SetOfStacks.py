import sys


class SetOfStacks:
    def __init__(self):
        self.piles = []
        self.stackIndex = -1

    def __str__(self):
        content = ''
        for l in self.piles:
            content += str(l) + '\n'
        return content

    def push(self, value):
        if len(self.piles) is 0 or len(self.piles[self.stackIndex]) >= 5:
            # Be careful with this case
            newStack = []
            newStack.append(value)
            self.piles.append(newStack)
            self.stackIndex += 1
        else:
            self.piles[self.stackIndex].append(value)

    def pop(self):
        if len(self.piles[self.stackIndex]) > 1:
            self.piles[self.stackIndex].pop()
        elif len(self.piles) is 0:
            return sys.maxsize
        else:
            value = self.piles[self.stackIndex].pop()
            self.piles.remove(self.piles[self.stackIndex])
            self.stackIndex -= 1
            return value


stack = SetOfStacks()
for i in range(100):
    stack.push(i)

print(stack)

for i in range(100):
    stack.pop()

print(stack)
