# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        self.front = head

        def check(back):

            if not back:
                return True

            if not check(back.next):
                return False

            if self.front.val != back.val:
                return False

            self.front = self.front.next

            return True

        return check(head)