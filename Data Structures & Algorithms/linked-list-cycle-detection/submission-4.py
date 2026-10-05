# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        fast = head.next
        slow = head

        while (fast and fast.next != None):
            fast = fast.next
            if (slow == fast):
                return True
            slow = slow.next
            fast = fast.next
        
        return False