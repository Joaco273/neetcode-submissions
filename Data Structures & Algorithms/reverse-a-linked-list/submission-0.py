# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        curr_node = head
        prev_node = None
        old_prev_node = None
        while curr_node.next != None:
            prev_node = curr_node
            curr_node = curr_node.next

            prev_node.next = old_prev_node
            old_prev_node = prev_node

        curr_node.next = prev_node
        head = curr_node
        return head 