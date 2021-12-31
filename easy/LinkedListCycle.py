from typing import Optional


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class LinkedListCycle:
	def hasCycle(self, head: Optional[ListNode]) -> bool:
		slow, fast = head, head

		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

			if slow == fast:
				return True
		return False

head = ListNode(3)
first = ListNode(4)
second = ListNode(0)
third = ListNode(2)

head.next = first
first.next = second
second.next = third
third.next = first

obj = LinkedListCycle()
print(obj.hasCycle(head))