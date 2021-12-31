from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class NthNodeFromEnd:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start, end = head, head
        while n > 0:
            end = end.next
            n -= 1

        while start.next is not end:
            start = start.next
        start.next = end.next

        return head
