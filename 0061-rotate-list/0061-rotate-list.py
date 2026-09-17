# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head
        temp = head
        length = 0
        while temp != None:
            length += 1
            temp = temp.next
        k = k % length
        if length == 0:
            return head
        temp1 = head
        temp2 = head
        for i in range(k):
            temp1 = temp1.next
        while temp1.next != None:
            temp1 = temp1.next
            temp2 = temp2.next
        temp1.next = head
        head = temp2.next
        temp2.next = None
        return head
