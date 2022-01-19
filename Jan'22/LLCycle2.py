from typing import Optional
# https://leetcode.com/problems/linked-list-cycle-ii/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LLCycle2:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        fast, slow = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
                
        if not fast or not fast.next:
            return None
        
        slow = head
        
        while fast != slow:
            fast = fast.next
            slow = slow.next
            
        return slow
    
obj = LLCycle2()
head = ListNode(1)
print(obj.detectCycle(head))