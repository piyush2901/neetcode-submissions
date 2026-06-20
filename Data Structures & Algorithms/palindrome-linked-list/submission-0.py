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

            # Go all the way to the end first
            if not check(back.next):
                return False

            # Now back is moving from tail toward head
            if self.front.val != back.val:
                return False

            # Move front forward
            self.front = self.front.next

            return True

        return check(head)