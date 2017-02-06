# Input: (B,D) (D,E) (A,B) (C,F) (E,G) (A,C)
# Output: (A(B(D(E(G))))(C(F)))

# Input: (A,B) (A,C) (B,D) (D,C)
# Output: E3

# E1: more than 2 children
# E2: duplicate edges
# E3: cycle present
# E4: multiple roots
# E5: any other errors

class Solution(object):
    def validBT(self, nodes):
        if len(nodes) is 0:
            return ''

        children_dict = {}
        for i in range(len(nodes)):
            if nodes[i] is '(':
                children_dict[nodes[i + 1]] = []
        for i in range(len(nodes)):
            if nodes[i] is '(':
                children_dict[nodes[i + 1]].append(nodes[i + 3])

        parent_dict = {}
        for i in range(len(nodes)):
            if nodes[i] is ')':
                parent_dict[nodes[i - 1]] = []
        for i in range(len(nodes)):
            if nodes[i] is ')':
                parent_dict[nodes[i - 1]].append(nodes[i - 3])
        for i in range(len(nodes)):
            if nodes[i] is '(' and nodes[i + 1] not in parent_dict.keys():
                parent_dict[nodes[i + 1]] = []

        root = None
        for k in parent_dict.keys():
            if len(parent_dict[k]) is 0:
                root = k

        for k in children_dict.keys():
            if len(children_dict[k]) > 2:
                return 'E1'
            if self.hasDup(children_dict[k]):
                return 'E2'

        if root is None:
            return 'E3'

        for k in parent_dict.keys():
            if len(parent_dict[k]) > 1:
                return 'E3'
        if self.hasMultiRoot(parent_dict):
            return 'E4'

        for k in children_dict.keys():
            children_dict[k].sort()
            if len(children_dict[k]) < 2:
                children_dict[k].append(None)
        for i in range(len(nodes)):
            if nodes[i] is ')' and nodes[i - 1] not in children_dict.keys():
                children_dict[nodes[i - 1]] = None
        return self.s_exp(children_dict, root)

    def hasDup(self, lis):
        d = {}
        for c in lis:
            d[c] = 0
        for c in lis:
            d[c] += 1
            if d[c] > 1:
                return True
        return False

    def hasMultiRoot(self, d):
        count = 0
        for k in d.keys():
            if len(d[k]) is 0:
                count += 1
            if count > 1:
                return True
        return False

    def s_exp(self, dict, root):
        if dict[root] is None:
            return '(' + root + ')'
        left = ''
        right = ''
        if dict[root][0] is not None:
            left = self.s_exp(dict, dict[root][0])
        if dict[root][1] is not None:
            right = self.s_exp(dict, dict[root][1])
        return '(' + root + left + right + ')'

if __name__ == '__main__':
    nodes = '(B,D) (D,E) (A,B) (C,F) (E,G) (A,C)'
    print(Solution().validBT(nodes))

    nodes = '(A,B) (A,C) (B,D) (D,C)'
    print(Solution().validBT(nodes))

    nodes = '(A,B) (A,C) (B,G) (C,H) (E,F) (B,D) (C,E)'
    print(Solution().validBT(nodes))

    nodes = ''
    print(Solution().validBT(nodes))

    nodes = '(A,B)'
    print(Solution().validBT(nodes))