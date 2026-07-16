# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        node = head
        
        while node and node.next:
            next_node = node.next

            while next_node and node.val == next_node.val:
                next_node = next_node.next

            node.next = next_node
            node = next_node
        
        return head