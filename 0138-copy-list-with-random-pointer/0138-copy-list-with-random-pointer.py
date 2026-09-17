"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head:
            temp = head
            mpp = {}
            while temp != None:
                newnode = Node(temp.val)
                mpp[temp] = newnode
                temp = temp.next
            temp = head
            while temp != None:
                copynode = mpp[temp]
                copynode.next = mpp.get(temp.next)
                copynode.random = mpp.get(temp.random)
                temp = temp.next
            return mpp[head]
            
