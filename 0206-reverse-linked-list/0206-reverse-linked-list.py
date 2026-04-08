# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next   # store next node
            curr.next = prev        # reverse link
            prev = curr             # move prev forward
            curr = next_node        # move curr forward
        
        return prev