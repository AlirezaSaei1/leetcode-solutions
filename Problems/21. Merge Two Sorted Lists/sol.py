# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = []
        while list1 and list2:
            if list1.val < list2.val:
                merged.append(list1.val)
                list1 = list1.next
            else:
                merged.append(list2.val)
                list2 = list2.next
        
        if list1:
            while list1:
                merged.append(list1.val)
                list1 = list1.next
        else:
            while list2:
                merged.append(list2.val)
                list2 = list2.next

        if merged:
            head = ListNode(merged[0])
            temp = head
            for i in range(1, len(merged)):
                temp.next = ListNode(merged[i])
                temp = temp.next
        
            return head

        else:
            return None
