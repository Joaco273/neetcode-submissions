# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        actual = dummy
        while list1 and list2:
            leftNum = list1.val
            rightNum = list2.val

            if leftNum <= rightNum:
                actual.next = list1
                list1 = list1.next
            else:
                actual.next = list2
                list2 = list2.next
            actual = actual.next
        
        if list1:
            actual.next = list1
        if list2:
            actual.next = list2
        
        return dummy.next

