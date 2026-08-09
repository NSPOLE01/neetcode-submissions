# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = l1
        carry = 0
        prev = None
        while l1 and l2:
            value = l1.val + l2.val + carry
            if value > 9:
                carry = value // 10
                value = value % 10
            l1.val = value
            prev = l1
            l1 = l1.next
            l2 = l2.next

        while l1:
            value = l1.val + carry
            if value > 9:
                carry = value // 10
                value = value % 10
            l1.val = value
            l1 = l1.next

        if carry != 0:
            prev.next = ListNode(carry)

        return dummy
        