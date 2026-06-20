# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2:
            return None
        
        if not list1:
            return list2

        if not list2:
            return list1

        ptr_1 = list1
        ptr_2 = list2

        new_list = ListNode()
        tail = new_list

        while ptr_1 != None and ptr_2 != None:

            if ptr_1.val <= ptr_2.val:
                new_list.val = ptr_1.val
                tail.next = ptr_1
                ptr_1 = ptr_1.next
            
            else:
                tail.next = ptr_2
                ptr_2 = ptr_2.next

            tail = tail.next

        
        if ptr_1:
            tail.next = ptr_1
        else:
            tail.next = ptr_2


        return new_list.next






