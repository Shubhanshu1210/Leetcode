# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        newhead = self.reverseList(slow)
        fisrt = head
        second = newhead
        while second != None:
            if fisrt.val != second.val:
                self.reverseList(newhead)
                return False
            fisrt = fisrt.next
            second = second.next
        self.reverseList(newhead)
        return True

