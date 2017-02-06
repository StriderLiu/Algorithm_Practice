# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None

        # # O(n) time, O(n) space
        # p, prev, dict = head, RandomListNode(head.label), {}
        # dict[p] = prev
        # dummy = RandomListNode(-1)
        # dummy.next = prev
        # p = p.next
        #
        # # Concatenate the new list (construct next)
        # while p:
        #     curt = RandomListNode(p.label)
        #     dict[p] = curt
        #     prev.next = curt
        #     prev = curt
        #     p = p.next
        #
        # # Construct random with dictionary (hash table)
        # p, curt = head, dummy.next
        # while p:
        #     if p.random:
        #         curt.random = dict[p.random]
        #     p, curt = p.next, curt.next
        #
        # return dummy.next

        # O(n) time, O(1) space
        # 1 -> 1' -> 2 -> 2' -> 3 -> 3' -> 4 -> 4'
        self.copyNext(head)
        self.copyRandom(head)
        return self.splitList(head)

        def copyNext(self, head):
            while head:
                node = RandomListNode(head.label)
                node.next = head.next
                head.next = node
                head = head.next.next

        def copyRandom(self, head):
            p, cp = head, head.next
            while p:
                if p.random:
                    cp.random = p.random.next
                p = p.next.next
                if p:
                    cp = p.next

        def splitList(self, head):
            newHead = head.next
            while head:
                temp = head.next
                head.next = head.next.next
                head = head.next
                if temp.next:
                    temp.next = temp.next.next
            return newHead


head = RandomListNode(1)
node1 = RandomListNode(2)
node2 = RandomListNode(3)
head.next, head.random = node1, node2
node1.next = node2
node2.random = head
print(Solution().copyRandomList(head).label)
