# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Step 1: Dummy node create
        dummy = ListNode(0)
        dummy.next = head
        
        fast = dummy
        slow = dummy
        
        # Step 2: Fast ko n steps aage le jao
        for _ in range(n):
            fast = fast.next
        
        # Step 3: Dono ko move karo jab tak fast last pe na aa jaye
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Step 4: Delete node
        slow.next = slow.next.next
        
        return dummy.next