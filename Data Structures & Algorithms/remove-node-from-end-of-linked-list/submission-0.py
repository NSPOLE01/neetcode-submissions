# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None

        temp = head
        size = 0
        while temp:
            size += 1
            temp = temp.next

        val = size-n

        if n == 0:
            return head.next

        cur = head
        for i in range(size - 1):
            if (i + 1) == val:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head



        