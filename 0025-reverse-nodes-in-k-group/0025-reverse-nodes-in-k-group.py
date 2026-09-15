# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getknode(self, temp, k):
        k -= 1
        while temp != None and k>0:
            k -=1
            temp = temp.next
        return temp
    def reversell(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
    
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        temp = head
        prevlast = None
        while temp != None:
            kthnode = self.getknode(temp, k)
            if kthnode == None:
                if prevlast:
                    prevlast.next = temp
                break
            nextnode = kthnode.next
            kthnode.next = None
            self.reversell(temp)
            if temp == head:
                head = kthnode
            else:
                prevlast.next = kthnode
            prevlast = temp
            temp = nextnode
        return head