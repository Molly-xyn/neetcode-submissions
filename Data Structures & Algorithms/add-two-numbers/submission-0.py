# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        n = 0
        curr1, curr2 = l1, l2
        while curr1 or curr2 or n:
            c1 = curr1.val if curr1 else 0
            c2 = curr2.val if curr2 else 0
            curr = c1 + c2 + n
            n = curr // 10
            tail.next = ListNode(curr % 10)
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
            tail = tail.next
        return dummy.next