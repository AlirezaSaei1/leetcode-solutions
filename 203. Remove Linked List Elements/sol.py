# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        flag = True

        while node:
            if node.next:
                if node.next.val == val:
                    skip_node = node.next.next
                    node.next = skip_node
                    flag = False
            if flag:
                node = node.next
            flag = True
        
        return dummy.next
