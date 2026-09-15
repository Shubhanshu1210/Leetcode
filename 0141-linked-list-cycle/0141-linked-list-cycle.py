# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        mpp = {}
        count = 0
        while temp is not None:
            if temp in mpp:
                return temp
            mpp[temp] = count
            count += 1
            temp = temp.next
        return False
