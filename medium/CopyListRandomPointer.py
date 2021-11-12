'''
https://leetcode.com/problems/copy-list-with-random-pointer/
A linked list of length n is given such that each node contains an additional random pointer,
which could point to any node in the list, or null.

Construct a deep copy of the list.
'''
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class CopyListRandomPointer:
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        old = head
        new = Node(old.val, None, None)
        self.visited[old] = new

        while old != None:
            new.random = self.getClonedCopy(old.random)
            new.next = self.getClonedCopy(old.next)

            old = old.next
            new = new.next

        return self.visited[head]

    def getClonedCopy(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None