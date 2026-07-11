# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        cur = 0

        node = head
        while node:
            cur = (cur << 1) | node.val
            node = node.next
        
        return cur