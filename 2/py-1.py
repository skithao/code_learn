# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current = dummy = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            value = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carry = value // 10
            val = value % 10

            current.next = ListNode(val)
            current = current.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next