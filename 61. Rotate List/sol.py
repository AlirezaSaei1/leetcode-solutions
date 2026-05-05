# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # 1. Find length and the actual tail
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
            
        # 2. Normalize k
        k = k % n
        if k == 0:
            return head
            
        # 3. Connect tail to head to form a ring
        old_tail.next = head
        
        # 4. Find new tail: (n - k - 1) steps from head
        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next
            
        # 5. Break the ring
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head