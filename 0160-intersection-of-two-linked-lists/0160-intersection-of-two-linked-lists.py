# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """

        a = headA
        b = headB

        while a != b:
            # If a reaches end, move to headB
            a = a.next if a else headB

            # If b reaches end, move to headA
            b = b.next if b else headA

        return a