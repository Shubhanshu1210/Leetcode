# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp != None:
            count+=1
            temp = temp.next
        if count == n:
            new_head = head.next
            return new_head
        res = count-n
        temp = head
        while temp != None:
            res-=1
            if res == 0:
                break
            temp = temp.next
        del_node = temp.next
        temp.next = temp.next.next
        return head